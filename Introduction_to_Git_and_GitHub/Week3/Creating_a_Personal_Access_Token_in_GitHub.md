# Creating a Personal Access Token in GitHub

Personal access tokens are used in place of your GitHub password at the command-line. To use a personal access token, you must first create one. The following is a step-by-step guide on how to create a personal access token in GitHub which will be used in the next lab, Qwiklabs Assessment: Introduction to GitHub. 

## Steps to creating a personal access token in GitHub

1. Log into your GitHub account with your username and password.
2. In the upper right hand corner click on your profile picture. 

![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/8Q7jQI_qRg2TdABAEiPfGw_a255fee890664af290776e778fc19ff1_image.png?expiry=1707004800000&hmac=qw2CgOgLNB_5ImDJVKaIcAv44WM93IxKFIvFnzV_hKo)

3. Use the drop-down menu, and click on Settings.

![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/cuty5FqMSYiirikwe5ervA_5785599e10b548c18c3105b5b5595af1_image.png?expiry=1707004800000&hmac=ZO-Zy9Dk-YhRksDGOS2JXNU8f-5lu2zHnAqkCtZZtOA)

4. On the left sidebar, click on Developer Settings. It looks like this:

![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/GIy7Uj9tRMWbQ0K6cTS3Xg_f83df98e187e4be8a833e4b46f2be8f1_image.png?expiry=1707004800000&hmac=yEnRZ1Jte1wSLJBrB5pG8iTpds1tnCHcZVYk20GlxPs)

5. On the left sidebar, click on Personal access tokens. Choose tokens (classic).

![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/oz7DyXjnSZqV5bhiScaBeA_690528d2e1ca49279b2cdf3dba1e70f1_image.png?expiry=1707004800000&hmac=25XvGavUJN4XKQ6sMcSpp7WZXPZ6ac_NM3fJFWm-SvE)

6. Click Generate new token. Choose Generate new token (classic).

![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/eId18dW0S-qV06eYg61gWQ_02c382744a584cbca5f781d1da9669f1_image.png?expiry=1707004800000&hmac=tlq9FPWtSzbfeAa2rLvJ6On6Rb1oYZSTxHOTOPiw4sk)

7. In the “Note” field, give your token a name. 
8. Set when you want your token to expire.
9. Select the scopes you want to grant this token. For the lab that follows make sure you select repo so that you can access repositories from the command-line. 

![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/6ILZ4N01QU6c_PH7DvzlOA_63281ffc5e6a4e8bacfde09945585df1_image.png?expiry=1707004800000&hmac=rJ_TpYs2ScHfcQnpbp4Mw1pT54Gng9nZ3dCfPRS-8ug)

10. Click Generate token.
11. Copy your new token to your clipboard. You may want to paste it in a document or note that you will delete after you have completed the lab. You will not be able to see the token again. 
12. Finally, when you go to login to your GitHub account at the command-line use your GitHub username and the token you just generated for your password. 

Here is the [official documentation](https://docs.github.com/en/enterprise-server@3.4/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) for creating personal access tokens from GitHub. 