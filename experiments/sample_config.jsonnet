local root = "path/to/root/"; # row path
local pathgen(path) = root + path;
{
    "input_path": pathgen("input.pdf"), # pdf path on which you want to sign
    "save_path": pathgen("output.pdf"), # save path you want to save
    "img_path": pathgen("inkan.png"), # img path which you want to put on the pdf
    "obj_pages": [1, 3], # List of page numbers you want to put. This is 1-indexed.
    "position": [147, 225], # The position List(mm)[width, height] to put image. The origin point is the lower left corner.
    "img_size": [20, 20] # List(px)[width, height] you want to resize.
}