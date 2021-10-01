# TreeCoverLoss_predictor
Prediction of tree cover loss based on the relaese of CO2 and other gases

I have used a datset from Kaggle to predict tree cover loss based on the Release of CO2 an other gases(in mg). The dataset actually consisted of other features as well
Country, Year were additional features present in the dataset. I used Random Forest regressor to calculate the feature importance. At that time I realised that Country and Year
have very less importance. Thus I decided to exclude them while training a ML model. I used Linear Regression as classifier because this is a 'prediction problem'. The model yieds
a good accuracy.

I have deployed this on heroku. I have made use of flask. Here is the link : https://todo-flaskprojecttcl.herokuapp.com/

I had a Requirements.txt file for this but I forgot to setup a virtual enviornmwnt from the beginning :P. There were just too many unecessary packages to be installed. So I have
not provided one. But the requirements are farely basic and if not present, you could simply pip install them. Hope you find it good.
**Hope you like it, Feel Free To Contribute**
