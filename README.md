# ENMailer

ENMailer is a python library that can send notes to Evernote email address.

<br>

* [ENMailer](#enmailer)
  * [Prerequisite](#prerequisite)
     * [sendmail](#sendmail)
  * [Installation](#installation)
  * [Quick Running Sample](#quick-running-sample)
  * [Usage in Detail](#usage-in-detail)
     * [&gt; Initialization](#-initialization)
     * [&gt; Setting Dispatcher and Recipient](#-setting-dispatcher-and-recipient)
     * [&gt; Title and Notebook Settings](#-title-and-notebook-settings)
     * [&gt; Writing Contents](#-writing-contents)
     * [&gt; Send](#-send)
     * [&gt; One-Line Initialization](#-one-line-initialization)
     * [&gt; SMTP Advanced Settings](#-smtp-advanced-settings)
  * [HTML on Evernote](#html-on-evernote)
     * [&gt; Using Heading Tags](#-using-heading-tags)
     * [&gt; Adding Styles to &lt;div /&gt;](#-adding-styles-to-div-)
     * [&gt; Adding Checkbox](#-adding-checkbox)
     * [&gt; Adding Horizontal Line](#-adding-horizontal-line)
     * [&gt; Bold, Italic, Strike-through](#-bold-italic-strike-through)
     * [&gt; Creating Table](#-creating-table)
  * [Acknowledgement](#acknowledgement)


<br><br>

## Prerequisite

<br>

### sendmail

This module relies on SMTP server. If your system doesn't have any SMTP server ready, I strongly recommend you to install sendmail on it. You can install sendmail by the following command:

```
$ sudo apt install sendmail
```

You also have to modify your **/etc/hosts**.

```
$ sudo nano /etc/hosts
```

Modify the line that starts with **127.0.0.1** to the following:

```
127.0.0.1 localhost.localdomain localhost YOUR_HOSTNAME
```

Be careful: **YOUR_HOSTNAME** is literally **your** hostname. If you don't know what this is, then you can check it out by running the following command on your terminal:

```
$ hostname
```

<br>

## Installation

You can easily install the module by using pip:

```
sudo pip3 install enmailer
```

<br>

## Quick Running Sample

``` python
from enmailer import ENMailer

mailer = ENMailer()

mailer.set_dispatcher("DISPATCHER")
mailer.set_recipient("EVERNOTE_EMAIL")
mailer.set_title("NOTE TITLE")

mailer.write_text("Note body.")
mailer.send()
```

<br>

## Usage in Detail

<br>

### > Initialization

Load ENMailer class and initialize:

``` python
from enmailer import ENMailer

mailer = ENMailer()
```

<br>

### > Setting Dispatcher and Recipient

``` python
mailer.set_dispatcher("your_email@example.com")
mailer.set_recipient("your_evernote_email@m.evernote.com")
```

**DISPATCHER** is the email account that Evernote will regard as the author of the article. It can be anything, as long as it is in appropriate email format.


**RECIPIENT** is the Evernote email address. This **is not** the email account that you use to login. Every Evernote account has its own unique email address - an adress that ends up with **@m.evernote.com**. You can find your address in `Settings` - `Email Notes to`.

<br>

### > Title and Notebook Settings

``` python
mailer.set_title("Your Note Title")
mailer.set_notebook("YOUR NOTEBOOK")
```

`set_notebook` method let you set your saving path. By default, the article will be saved in your default notebook.

<br>

### > Writing Contents

There are two types of writing text. One is using plain text, the other is using HTML format. The method you need is `write_text()` and `write_html()` respectively. Be aware of the fact that both method overwrites the previous value.

``` python
# Using plain text
TEXT = "Our world is worth fighting for."
mailer.write_text(TEXT)

# Using HTML
HTML = """
<div style="font-size:24px; font-weight: bold;">
Our world is worth fighting for.
</div>
"""
mailer.write_html(HTML)
```

For those who wonder the usage of HTML, please read the **HTML on Evernote** below.

<br>

### > Send

Finally, once you write data on your class file, you need to call `send()` module:

``` python
mailer.send()
```

If it doesn't throw any error, then Ta-da! You made it!

<br>

### > One-Line Initialization

You can also set settings on initialization as well:

``` python
mailer = ENMailer(dispatcher="SENDER_EMAIL",
                  recipient="EVERNOTE_EMAIL",
                  notebook="NOTEBOOK_NAME",
                  title="NOTE TITLE",
                  contents="Note body.")
```

<br>

### > SMTP Advanced Settings

By default, ENMailer uses localhost port 25 for SMTP Server connection. If you want to use other settings, then here's the magic code:

``` python
HOST = 'localhost'  # <str>
PORT = 25           # <int>

mailer = ENMailer(SMTP_port=PORT,
                  SMTP_host=HOST)
```

<br>

## HTML on Evernote

Evernote limits certain types of HTML, since it is designed to store static text data. So if you are trying to be more specific on visualization, I recommend you to take a look at this paragraph. Below are sample HTML code snippets.

<br>

### > Using Heading Tags

``` html
<h1>H1 for font-size 28</h1>
<h2>H2 for font-size 21</h2>
<h3>H3 for font-size 16</h3>
<h4>H4 for font-size 14</h4>
<h5>H5 for font-size 11</h5>
<h6>H5 for font-size 9</h6>
```

<br>

### > Adding Styles to &lt;div /&gt;

You can apply most of the CSS that regards styles of a text:

``` html
<div style="color:#900020;
            font-size: 48px;
            font-family: 'Times New Roman';
            text-align: right;
            margin-right: 140px;
            margin-left: 140px;">
Text with styles
</div>
```

<br>

### > Adding Checkbox

``` html
<div>
    <input disabled="true" class="en-todo" type="checkbox">
    Sample list
</div>
<div>
    <input disabled="true" class="en-todo" type="checkbox" checked="true">
    Completed Sample list 
</div>
```

### > Adding Horizontal Line

``` html
<hr>
```

<br>

### > Bold, Italic, Strike-through

``` html
<b>Bold Tag</b>
<div style="font-weight: bold;">Bold from CSS</div>

<i>Italic Tag</i>
<div style="font-style: italic;">Italic from CSS</div>

<s>Strike-through Tag</s>
<div style="text-decoration: line-through;">Strike-through from CSS</div>
```

<br>

### > Creating Table

Caution: This is not an Evernote's new type table. Rather it is a fixed size table, using old HTML.

``` html
<table>
<tr>
    <th>Input HCl (ml)</th>
    <th>Total HCl (ml)</th>
    <th>pH</th>
</tr>
<tr>
    <td>3</td>
    <td>0</td>
    <td>11.6</td>
</tr>
<tr>
    <td>3</td>
    <td>3</td>
    <td>10.93</td>
</tr>
</table>
```

<br>

## Acknowledgement

I appreciate Stack Overflow for solving countless errors and bugs, and tons of coffee for overclocking myself.

