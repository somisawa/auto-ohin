local root = "experiments/";
local pathgen(path) = root + path;
{
    "input_path": pathgen("sample_input.pdf"),
    "save_path": pathgen("output.pdf"),
    "img_path": pathgen("inkan.png"),
    "obj_pages": [1, 3],
    "position": [147, 225],
    "img_size": [20, 20]
}