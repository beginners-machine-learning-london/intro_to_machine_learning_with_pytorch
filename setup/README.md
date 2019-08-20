# Installations

You are required to download and install the following free software for this workshop.

- [Anaconda Package Manager](https://www.anaconda.com/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Git Version Control System](https://git-scm.com/)

## Setting up your conda environment

When you download and install Anaconda, you will install the latest version of Python, Jupyter Notebooks, and several useful data science libraries that are essential for data manipulation and developing machine learning applications.

Anaconda's main benefit is that enables you to setup your own development environment. Often you will need to work with a specific version of Python and associated packages depending on the project requirements. In this way, having the ability to create new environments and switching between them may reduce unnecessary errors. In addition, using a development environment enables you to run other people's code or publish your own.

To create a new environment, start the `Anaconda Prompt` and execute the following code to create your own environment.

*Code to enter* Note that you must enter the code that I have written on the line below the first instance of ```conda```in each block. E.g., ```conda create --name my_env```.

```conda
conda create --name my_env

Solving environment: done
## Package Plan ##

  environment location: C:\Users\Username\Anaconda3\envs\my_env

Proceed ([y]/n)? y
```

## Testing your environment

Test that you have successfully created a new environment by entering the below. If correctly installed, this will activate the new environment:

```conda
conda activate my_env

(my_env) C:\Users\Username>
```

Check what packages have been already installed within your environment by entering:

```conda
conda list my_env

# packages in environment at C:\Users\Username\Anaconda3\envs\my_env:
#
# Name                    Version                   Build  Channel
attrs                     19.1.0                   py37_1
backcall                  0.1.0                    py37_0
ca-certificates           2019.1.23                     0
...                        ...                        ...
webencodings              0.5.1                    py37_1
wheel                     0.33.1                   py37_0
wincertstore              0.2                      py37_0
zlib                      1.2.11               h62dcd97_3
```

```conda
(my_env) C:\Users\Username>
```

After the above steps, run the below commands to install the packages that the workshop requires.

#### Installing Numpy

```conda
conda install numpy
```

#### Installing Matplotlib

```conda
conda install matplotlib
```

#### Installing Pytorch - WINDOWS

```conda
conda install pytorch-cpu torchvision-cpu -c pytorch
```

#### Installing Pytorch - MacOS

To install pytorch for MacOS you will need to run the following command instead:

```
conda install pytorch torchvision -c pytorch
```

#### Test Pytorch Installation

Check one last time that you have everything installed and ready to go using:

```conda
conda list
```
To verify that you have successfully installed Pytorch, you may import the `torch` and `torchvision` packages in your python console. If you don't get any errors, you have successfully installed Pytorch.

## Installing Jupyter Notebooks

1. Open the `Anaconda Navigator`
2. Select your newly created environment `my_env` from the top drop down menu on the main page
3. Press the `install` button underneath the Jupyter Notebooks card. 
4. After installation, press the `launch` button to start the Jupyter notebooks on your browser. 
5. Navigate to the notebook files we have provided in this repo to open the notebook.

## Starting VS Code via Anaconda Navigator

To ensure that your VS code is configured to your environment `my_env`, simply launch VS Code via `Anaconda Navigator` while after selecting your environment from the drop down menu.

## Learn More

- [Setting up conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#viewing-a-list-of-your-environments)
- [Codecademy - How to work with Jupyter notebooks - 11 min watch](https://www.codecademy.com/articles/how-to-use-jupyter-notebooks)
