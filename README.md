# ENMailer

ENMailer is a python library that can send notes through Evernote email address.

## Prerequisites

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

Be careful: **YOUR_HOSTNAME** is literally **your** hostname. If you don't know what this is, then you can check it out by running the following command:

```
$ hostname
```

## Installation

You can easily install the module by using pip:

```
sudo pip3 install enmailer
```

## Getting Started

### Quick Example

```
from enmailer import ENMailer

mailer = ENMailer()

mailer.set_dispatcher("SENDER_EMAIL")
mailer.set_recipient("EVERNOTE_EMAIL")
mailer.set_title("NOTE TITLE")

mailer.write_text("Note body.")
mailer.send()
```

## Settings on Initialization

You can set settings on initialization as well:

```
mailer = ENMailer(dispatcher="SENDER_EMAIL",
                  recipient="EVERNOTE_EMAIL",
                  notebook="NOTEBOOK_NAME",
                  title="NOTE TITLE",
                  tags=['tagA', 'tagB'],
                  contents="Note body.")
```

