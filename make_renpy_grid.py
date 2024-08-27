import sys
import os


# Creates a grid 

# Requires grid_label_template.rpy
# Todo: allow comments in template file that aren't included, or are prepended (once only)

"""

necessary information:
sys.argv[1]: Filename (name of area)
sys.argv[2]: 2D or 3D
sys.argv[3]: x min-max
sys.argv[4]: y min-max
sys.argv[5]: y min-max
sys.argv[6]: z min-max (3D only)
"""


def main():

    min_dimension = 0
    max_dimension = 200

    # Check number of arguments
    if len(sys.argv) < 5:
        sys.exit("Too few command-line arguments\n")
    if len(sys.argv) > 6:
        sys.exit("Too many command-line arguments\n")

    # Check 2D or 3D
    dimensions = get_number_of_dimensions(sys.argv[2])

    # Check number of arguments for 2D or 3D
    if dimensions == 2 and len(sys.argv) != 5:
        sys.exit("2D requires x and y\n")
    if dimensions == 3 and len(sys.argv) != 6:
        sys.exit("3D requires x, y, and z\n")
    
    # Get x dimensions    
    x = sys.argv[3]
    x_min, x_max = get_dimensions_range(x, min_dimension, max_dimension)
    # Get y dimensions
    y = sys.argv[4]
    y_min, y_max = get_dimensions_range(y, min_dimension, max_dimension)
    # Get z dimensions for 3D
    if dimensions == 3:
        z = sys.argv[5]
        z_min, z_max = get_dimensions_range(z, min_dimension, max_dimension)
    else:
        z_min = 0
        z_max = 0

    # Get area / output filename
    area = get_area(sys.argv[1])
    filename = f"{area}.rpy"

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
    for k in range(z_min, z_max+1):
        for j in range(y_min, y_max+1):
            for i in range(x_min, x_max+1):
                if dimensions == 2:
                    label = f"{area}_{i}_{j}"
                else:
                    label = f"{area}_{i}_{j}_{k}"
                f.write(f"label {label}:")
                f.write("\n\n")
                f.write(template)
                f.write("\n\n")
    f.close()
    f2.close()

def get_number_of_dimensions(dimensions):
    if dimensions in ["2", "2D", "2d"]:
        return 2
    elif dimensions in ["3", "3D", "3d"]:
        return 3
    else:
        sys.exit("Must be 2D or 3D") 

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

def get_dimensions_range(dimensions, min_dimension, max_dimension):
    dimensions = dimensions.split("-")
    if len(dimensions) != 2:
        sys.exit("Dimensions format: min-max")
    try:
        min = int(dimensions[0])
        max = int(dimensions[1])
    except ValueError:
        sys.exit("Dimensions format: min-max")
    if min < min_dimension:
        sys.exit(f"Min dimension is {min_dimension}")
    if max > max_dimension:
        sys.exit(f"Max dimension is {max_dimension}")
    if min > max:
        sys.exit("Dimensions format: min-max")
    return min, max


if __name__ == "__main__":
    main()
