import sys
import os

# Creates a region

# Requires grid_label_template.rpy
# Todo: allow comments in template file that aren't included, or are prepended (once only)

"""

necessary information:
sys.argv[1]: Filename (name of area)
sys.argv[2]: x min-max
sys.argv[3]: y min-max
sys.argv[4]: z min-max (3D only)

"""


class Region_info():
    def __init__(self):
        self.name = ""
        self.x_min = 0
        self.x_max = 0
        self.y_min = 0
        self.y_max = 0
        self.z_min = 0
        self.z_max = 0

def main():

    region_info = get_region_info(sys.argv)

    filename = f"{region_info.area}.rpy"

    # Open output file
    try:
        f = open(filename, "w")
    except OSError:
        try:
            f = open(filename, "x")
        except OSError:
            sys.exit("Could not create file")

    # Open label template
    try:
        f2 = open("grid_label_template.rpy", "r")
    except OSError:
        sys.exit("Could not open grid_label_template.rpy")
    template = f2.read()
    header = ""
    f.write(header)
    for k in range(region_info.z_min, region_info.z_max+1):
        for j in range(region_info.y_min, region_info.y_max+1):
            for i in range(region_info.x_min, region_info.x_max+1):
                label = f"{region_info.area}_{i}_{j}_{k}"
                f.write(f"label {label}:")
                f.write("\n\n")
                f.write(template)
                f.write("\n\n")
    f.close()
    f2.close()

def get_region_info(args):

    # Check number of arguments
    if len(args) < 5:
        sys.exit("Too few command-line arguments\n")
    if len(args) > 5:
        sys.exit("Too many command-line arguments\n")

    region_info = Region_info()

    # Get area / output filename
    region_info.area = get_area(sys.argv[1])    
    # Get x dimensions
    x = sys.argv[2]
    region_info.x_min, region_info.x_max = get_dimensions_range(x)
    # Get y dimensions
    y = sys.argv[3]
    region_info.y_min, region_info.y_max = get_dimensions_range(y)
    # Get z dimensions for 3D
    z = sys.argv[4]
    region_info.z_min, region_info.z_max = get_dimensions_range(z)

    return region_info

def get_area(area):
    if area.find(".") != -1:
        sys.exit("Area/filename must not include '.' or '.rpy' extension")        
    if area.find("-") != -1:
        sys.exit("Area/filename must not include '-'")
    area = area.strip()
    if len(area) == 0:
        sys.exit("Needs area/filename")
    if len(area) > 54:
        sys.exit("Area/filename too long")
    if os.path.isfile(f"{area}.rpy"):
        while True:
            overwrite = input("File already exists. Overwrite? (y/n) ").strip().lower()
            if overwrite == "y":
                return area
            elif overwrite == "n":
                sys.exit("Aborted\n")
    return area

def get_dimensions_range(dimensions):
    min_dimension = 0
    max_dimension = 200

    dimensions = dimensions.split("-")

    if len(dimensions) == 1:
        dimensions = ["0", dimensions[0]]
    elif len(dimensions) != 2:
        sys.exit("Dimensions format: max or min-max")
    
    try:
        min = int(dimensions[0])
        max = int(dimensions[1])
    except ValueError:
        sys.exit("Dimensions format: max or min-max")

    if min < min_dimension:
        sys.exit(f"Min dimension is {min_dimension}")
    if max > max_dimension:
        sys.exit(f"Max dimension is {max_dimension}")
    if min > max:
        sys.exit("Dimensions format: max or min-max")

    return min, max

if __name__ == "__main__":
    main()