# auto-ohin

You can ohin on the input pdf easily.

## Installation

`pip install auto-ohin`

## Requirement

```python = "^3.7"
Pillow = "^8.0.1"
reportlab = "^3.5.55"
PyPDF4 = "^1.27.0"
jsonnet = "^0.16.0"
```

## Usage

### 1. First you only need config files like below.

```jsonnet
local root = "path/to/root"; # row path
local pathgen(path) = root + path;
{
    "input_path": pathgen("input.pdf"), # pdf path on which you want to sign
    "save_path": pathgen("output.pdf"), # save path you want to save
    "img_path": pathgen("inkan.png"), # img path which you want to put on the pdf
    "obj_pages": [1, 3], # List of page numbers you want to put. This is 1-indexed.
    "position": [147, 225], # The position List(mm)[width, height] to put image. The origin point is the lower left corner.
    "img_size": [20, 20] # List(px)[width, height] you want to resize.
}
```

### 2. Run simply in commandlines.
```bash
auto-ohin path/to/config.jsonnet
```

## Author

* Sota Misawa (mitawaut)
* mathematical engineering faculty of UTokyo
* E-mail: so.misawa.research@gmail.com

## License
"auto-ohin" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).