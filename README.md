# Deep Learning for Computer Vision
These are the practical sessions and homeworks for the UCU computer vision class. 

J. Matias Di Martino
<matias.di.martino.uy@gmail.com>

## Installation and preliminars
To do these practical sessions you will need to learn (a) how to use git and (b) how to use conda to create and manage environments. If you are not familiar with these tools, please check online tutorials and make sure you (i) have a github account with key pairs so you can clone and push using ssh, (ii) have conda intalled. If you are somehow familiar with these tools, check the cheat sheets in the `cheat sheets` folder for a quick reminder. 

### Creating a conda environment

```bash
conda create --name dlfcv2025 python=3.10
```
To activate the environment, run:
```bash
conda activate dlfcv2025
```

To deactivate the environment, run:
```bash
conda deactivate
```

To install the dependencies for this course, run:
```bash
pip install -r requirements.txt
```

To install a specific package, run:
```bash
pip install <package_name>
```

To check the installed packages in the environment, run:
```bash
pip freeze
```
