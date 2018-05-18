# Kiwi Challenge

This is a repository for implement a solution for [Kiwi Challenge](https://github.com/KiwiCampusChallenge/Kiwi-Campus-Challenge/blob/master/Deep-Learning-Challenge.md)

## Usage

1. Download and extract dataset

		$ python app.py download

2. For train model

		$ python app.py train -m LRSL -d ./images/train/

3. For test model

		$ python app.py test -m LRSL -d ./images/test/

4. For infer a image

		$ python app.py infer -m LRSL -d ./images/test/0000003.ppm
