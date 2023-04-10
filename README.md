# VideoGPT
Natural language video editing with GPT-3 

## **This is en experimental home project, and is for testing or entertainment purposes only. It may contain bugs**

## REQUIREMENTS

Tested on Linux Ubuntu, that requires `ImageMagick` to be installed, so:

`sudo apt update && sudo apt install imagemagick`

Then you have to uncomment or remove the following line in the `/etc/ImageMagick-6/policy.xml` file:

```xml
<policy domain="path" rights="none" pattern="@*"/>
```

If you don't want to remove it, you can just uncomment in this way:

```xml
<!-- <policy domain="path" rights="none" pattern="@*"/> -->
```
Save.

Then:

`git clone https://github.com/0ut0flin3/VideoGPT`

`cd VideoGPT`

`pip install -r requirements.txt`

`python3 main.py /path/to/yourvideo.mp4`

Replace the path with the path of the video that you want to edit, then type the action you want to perform on the video:

```console
user@linux:~VideoGPT$ python3 main.py ./test.mp4
What you would like to do with this video?

> Add the text "LOL" at second 5 with a duration of 3 seconds
```

if you're lucky, you'll find your edited video in the `outputs` folder. Original video will not be touched.

Often runs into bugs and syntax errors, will be fixed. Pull requests for improvements are welcome




