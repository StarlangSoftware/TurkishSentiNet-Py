Turkish Sentiment Lexicon (HisNet)
============

Exploiting a dictionary-based method necessitates the construction of a specific polarity dictionary in the same language as the data-to-be-analyzed. The reason behind this necessity stems from the improbability of creating a universal polarity dictionary due to both grammatical and cultural asymmetries between languages. For instance, a certain historical event can have positive connotations in one culture and negative connotations in another culture. Thus, it is an essential step to create a language specific polarity dictionary.

In this study, we present a polarity dictionary to provide an extensive polarity dictionary for Turkish that dictionary-based sentiment analysis studies have been longing for. Our primary objective is to provide a more refined and extensive polarity dictionary than the previous SentiTurkNet. In doing so, we have resorted to a different network from the referenced study. We have identified approximately 76,825 synsets from Kenet, which then were manually labeled as positive, negative or neutral by three native speakers of Turkish. The first labelling process resulted in 3,100 positive, 10,191 negative and 63,534 neutral data, during which decisions were based on the meaning and connotation of each word. 

Subsequently, a second labeling was further made on positive and negative words as strong or weak based on their degree of positivity or negativity. For instance, the word mükemmel (excellent) in Turkish has been marked three times. Thus, three different views were obtained for the value of this word. While selecting the appropriate label, the compatibility of the labels selected by the three labelers was also evaluated. To put it differently, if a positive word receives strong label from all three annotators, it is regarded as strong positive. If it receives two strong and one weak label, it is considered as very positive. If it is la- belled as strong once and as weak twice, it means it is just positive. Finally, if it receives weak label from all three annotators, it is considered as weak positive. The same is also true for the words labelled as negative.

|Polarity Level|# of Synsets|
|---|---|
|Strongly positive|1,038|
|Very positive|451|
|Positive|456|
|Weakly positive|1,234|
|Objective|63,534|
|Strongly negative|4,430|
|Very negative|1,465|
|Negative|1,238|
|Weakly negative|3,360|

For Developers
============

You can also see [Cython](https://github.com/starlangsoftware/TurkishSentiNet-Cy), [Java](https://github.com/starlangsoftware/TurkishSentiNet), [C++](https://github.com/starlangsoftware/TurkishSentiNet-CPP), [Swift](https://github.com/starlangsoftware/TurkishSentiNet-Swift), or [C#](https://github.com/starlangsoftware/TurkishSentiNet-CS) repository.

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
