
PD = 0.2; %size of test dataset

cv = cvpartition(size(dataset,1),'HoldOut',PD);
Dtrain = dataset(cv.training,:);
Dtest = dataset(cv.test,:);


Xtrain = Dtrain(:, 2:7);
Ytrain = Dtrain(:,1);

Xtest = Dtest(:,2:7);
Ytest = Dtest(:,1);

clear PD;
clear cv;
clear Dtrain;
clear Dtest;
clear dataset;