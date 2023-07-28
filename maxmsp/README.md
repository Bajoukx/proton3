# Proton3 inside MaxMSP

In order to use the proton3 packages inside the [MaxMSP](https://cycling74.com/products/max) environment, at the moment is required to have the package installed into the base environment (following [this](https://github.com/Bajoukx/proton3#installation)).

## How to use

At the moment the MaxMSP patch ```node-proton3.maxpat``` is gonna use the ```node-proton3.js``` file in order to execute the ```script.py``` script containing the evaluation of a free particle at variable energy level.

If the file ```node-proton3.js``` is not found by your patch, make sure to drag and drop the script into the [file browser](https://docs.cycling74.com/max8/vignettes/file_browser) of MaxMSP.