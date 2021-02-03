For Developers
============

You can also see [Java](https://github.com/starlangsoftware/TurkishSentiNet), [C++](https://github.com/starlangsoftware/TurkishSentiNet-CPP), [Swift](https://github.com/starlangsoftware/TurkishSentiNet-Swift), or [C#](https://github.com/starlangsoftware/TurkishSentiNet-CS) repository.

## Requirements

* [Python 3.7 or higher](#python)
* [Git](#git)

### Python 

To check if you have a compatible version of Python installed, use the following command:

    python -V
    
You can find the latest version of Python [here](https://www.python.org/downloads/).

### Git

Install the [latest version of Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

## Download Code

In order to work on code, create a fork from GitHub page. 
Use Git for cloning the code to your local or below line for Ubuntu:

	git clone <your-fork-git-link>

A directory called SentiNet will be created. Or you can use below link for exploring the code:

	git clone https://github.com/starlangsoftware/TurkishSentiNet-Py.git

## Open project with Pycharm IDE

Steps for opening the cloned project:

* Start IDE
* Select **File | Open** from main menu
* Choose `TurkishSentiNet-PY` file
* Select open as project option
* Couple of seconds, dependencies will be downloaded. 

Detailed Description
============

+ [SentiNet](#sentinet)
+ [SentiSynSet](#sentisynset)

## SentiNet

Duygu sözlüğünü yüklemek için

	a = SentiNet()

Belirli bir alana ait duygu sözlüğünü yüklemek için

	SentiNet(fileName: str)
	a = SentiNet("dosya.txt")

Belirli bir synsete ait duygu synsetini elde etmek için

	getSentiSynSet(self, _id: str) -> SentiSynSet

## SentiSynSet

Bir SentiSynset elimizdeyken onun pozitif skorunu

	getPositiveScore(self) -> float

negatif skorunu

	getNegativeScore(self) -> float

polaritysini

	getPolarity(self) -> PolarityType
