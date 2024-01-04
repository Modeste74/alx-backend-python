<h1>0x03. Unittests and Integration Tests</h1>
<h2>UnitTests Back-end Integration tests</h2>
<p>Unit testing is the process of testing that a particular function returns expected results for different set of inputs. A unit test is supposed to test standard inputs and corner cases. A unit test should only test the logic defined inside the tested function. Most calls to additional functions should be mocked, especially if they make network or database calls.</p>
<p>The goal of a unit test is to answer the question: if everything defined outside this function works as expected, does this function work as expected?</p>

<p>Integration tests aim to test a code path end-to-end. In general, only low level functions that make external calls such as HTTP requests, file I/O, database I/O, etc. are mocked.</p>

<p>Integration tests will test interactions between every part of your code.</p>
<p>Execute your tests with</p>
<ul>
   <li>$ python -m unittest path/to/test_file.py</li>
</ul>
