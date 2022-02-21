BUCTOJ 用Python玩转北化OJ平台
========================================

.. .. image:: https://readthedocs.org/projects/buctoj/badge/?version=latest
..     :target: https://buctoj.readthedocs.io/zh_CN/latest/?badge=latest
..     :alt: 文档状态

.. image:: https://readthedocs.org/projects/buctoj/badge/?version=latest

将 `BUCT-OJ <https://buctcoder.com/>`_ 的一些功能封装成包，从而实现通过脚本提交代码等。

⚠ 仅供学习测试，不能用于特殊用途

⚠ 对于拥有管理员账号的同学，应该有自觉使用管理号的觉悟，不会用来免做题目

主要功能
=============

模拟登录
--------------------------


::

    from BUCTOJ import login
    cookies = login(用户名, 密码)


使用cookies中的session即可以账号身份进行操作

若账号密码错误，则返回cookie不可用

提交代码
--------------------------


::

    from BUCTOJ import submit
    submit(比赛的cid，要提交问题的pid，你的cookie，要提交的代码)



上述方式会使用C++语言进行提交(目前仅支持C++)

进入比赛的某道题目后，地址栏的url中会有cid和pid。

例如 `Contest2347` 的 `A` 题，url为 `https://buctcoder.com/problem.php?cid=2347&pid=0` ，因此此题目的cid为2374，pid为0

cookie是登录功能所获得的cookie。

自动完成一个比赛
--------------------------------

::

    from BUCTOJ import finish1contest
    finish1contest(比赛cid, 你的用户名, 你的密码, 管理员用户名, 管理员密码)

**前提**：

1. 拥有一个管理员账号

2. 每道题都有用C++通过者（非本次比赛提交也可）

**功能**：

若满足以上两个条件，则此函数具有以下功能：

1. 每隔大约15s通过一道题

2. 查重率为0

若某次比赛中一些题目无人用C++通过，则程序会跳过此题继续提交下一题

修改配置
=============


修改域名
--------------------------

脚本的默认oj域名为"https://buctcoder.com/"

若非本域名的其他相同oj平台，则可以进行配置其他域名。

假如"https://oj.letmefly.xyz/"也是采用的 `hustoj <https://github.com/zhblue/hustoj/>`_ ，那么此脚本可能也能用来进行oj.letmefly.xyz的操纵。

::

    from BUCTOJ import Config
    from BUCTOJ import login

    Config.set_info("base_url", "https://oj.letmefly.xyz/")
    cookies = login(0, 0)

当前仅支持“域名”这一个配置。
