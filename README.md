# pw_checker
A tool to check whether your password is secure.
<h2>Case 1:</h2>
Command:<br>
<code>python checkpassword.py thisismypassword</code>

Expected result:<br>
<code>Password: thisismypassword, was found 2940 times ... you should change your password!</code>
<br>
<h2>Case 2:</h2>
Command:<br>
<code>python checkpassword.py fdsfjkdhuehreuw834324</code>

Expected result:<br>
<code>Password: fdsfjkdhuehreuw834324, was NOT found. You can use it!</code>
<br>
<h2>Another version shown on my LinkedIn profile:</h2>
The program asks for password after it runs instead of running the program with the password typed in the terminal.<br>
Command:<br>
<code>python checkpassword.py</code>
Expected result:<br>
<code>What is your password to check? i am happy 1234</code>
<br>
<code>Password: i am happy 1234, was NOT found. You can use it!<code>
