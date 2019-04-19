<h1><strong><span style="text-decoration: underline;">Data Downloader</span></strong></h1>
<p>We used&nbsp;<a href="http://image-net.org/download-imageurls">ImageNet</a>&nbsp;dataset.</p>
<h2>Steps:</h2>
<h3>Locally</h3>
<ol>
<li>download url list (you can choose any link) from this <a href="http://image-net.org/download-imageurls">link</a></li>
<li>run in the terminal:&nbsp; <code> python3 txt_to_csv.py -t [url list txt file] -c [csv desired file name]&nbsp; -m [num of images to download]</code> this should output the csv file</li>
<li>run ./download.sh [csv_file path] [desired download dir]</li>
</ol>
<h3>Colab</h3>
<ol>
<li>Open file&nbsp;data_downloader.ipynb</li>
<li>Edit PROJECT_DIR variable to point to your project path in google drive</li>
<li>Run all&nbsp;</li>
</ol>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p><span style="text-decoration: underline;">Note:</span></p>
<p>We uploaded a sample url txt file and csv file&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
