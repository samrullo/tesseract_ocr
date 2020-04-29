# Introduction

## Bulk converting PDF file pages to images

<h4>Location of your windows ubuntu sub-system home folder</h4>
<p>C:\Users\amrul\AppData\Local\Packages\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\LocalState\rootfs\home\samrullo\uzbek_tili_izohli\pdf</p>
<h4>ImageMagick</h4>
<p>The tool that allows you to convert PDF pages to images is ImageMagick. You can find out about it from <a href="https://imagemagick.org/index.php">here</a></p>
<p>Once you install it on your ubuntu sub-system, <strong>convert</strong> command will be available.
And you can run following example command
</p>
<code>
sudo convert -density 150 uzbek_tilining_izohli_lugati_a_www.ziyouz.com.pdf -quality 90 output.png
</code>