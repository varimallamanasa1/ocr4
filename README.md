# Text-detection-using-heroku-english-hindi-marathi


### This repository consists of files required to deploy a Machine Learning Web App created with Flask on Heroku platform.

• If you want to view the deployed model, click on the following link:
Deployed at: https://image-to-text-sahil.herokuapp.com/

• __Problem Statement__:
  Detect English, Hindi and Marathi text from image. 

• __Dependencies__: <br />
    1.Python - 3.6 <br />
    2.Gunicorn==19.9.0 <br />
    3.Pytesseract <br />
    4.Numpy <br />
    5.Opencv <br />
    6.Flask - 1.1.1 <br />

• __Steps__: <br />
  1. Get input image from html and using OpenCV decode image.<br />
  2. Clean image use dilation and erosion technique. <br />
  3. Pass image to pytesseract. <br />
  4. Return detected text to html page
  
## Screenshots of the original website: <br /><br />
  ### 1st: HomePage of Website <br /><br />
  ![Screenshot (107)](https://user-images.githubusercontent.com/36062668/89508462-94165780-d7eb-11ea-8178-b1254513324a.png)


  ### 2nd: After entering image containing English text <br />
  ![Screenshot (108)](https://user-images.githubusercontent.com/36062668/89509600-22d7a400-d7ed-11ea-9a65-5eb1a8854da4.png) 
  <br />
  ![Screenshot (109)](https://user-images.githubusercontent.com/36062668/89509666-37b43780-d7ed-11ea-8289-fdedd507b8eb.png) 
  <br />
   ![Screenshot (48)](https://user-images.githubusercontent.com/36062668/89517403-47d11480-d7f7-11ea-8635-282e8274475b.png)
<br />
  

  ### 3rd: After entering image containing Hindi text
  ![Annotation 31](https://user-images.githubusercontent.com/36062668/89511824-04bf7300-d7f0-11ea-880a-326e8417b189.png)
  ![Annotation 32](https://user-images.githubusercontent.com/36062668/89512009-405a3d00-d7f0-11ea-9a5c-f7155883c9dc.png)

### 4th: After entering image containing Marathi text
  ![Annotation 33](https://user-images.githubusercontent.com/36062668/89512974-954a8300-d7f1-11ea-80ca-7b044c2a694b.png)



**Please do ⭐ the repository, if it helped you in anyway.**
