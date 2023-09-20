from lsecmail.helper import ISecMail


def main():
    i_sec_mail = ISecMail()

    # gen random mail box
    mails = i_sec_mail.gen_random_mail_box()

    print(mails)


if __name__ == '__main__':
    main()
