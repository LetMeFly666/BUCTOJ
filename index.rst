BUCTOJ 用Python玩转北化OJ平台
========================================

.. .. image:: https://readthedocs.org/projects/buctoj/badge/?version=latest
..     :target: https://buctoj.readthedocs.io/zh_CN/latest/?badge=latest
..     :alt: 文档状态

.. image:: https://readthedocs.org/projects/buctoj/badge/?version=latest

将 `BUCT-OJ <https://buctcoder.com/>`_ 的一些功能封装成包，从而实现通过脚本提交代码等。

⚠ 仅供学习测试，不能用于特殊用途

⚠ 对于拥有管理员账号的同学，应该有自觉使用管理号的觉悟，不会用来免做题目

主要供BUCTOJ管理员使用

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

通过id提交代码
--------------------------


::

    from BUCTOJ import submitById, login
    submit(login(账号，密码)，题目id，代码，语言)
    # response = submit(login('LetMeFly', 'SoHandsome'), '6264', """#include <bits/stdc++.h>\n...""", 'C++')
    # response = submit(login('LetMeFly', 'SoHandsome'), '6264', """#include <bits/stdc++.h>\n...""", '1')



上述方式支持多种语言提交，可以传参languageid(对应的languageid在BUCTOJ的提交页面)，也可传参语言名。当语言名不受支持时会认为传递的参数是languageid。

语言、id对照表：

+-----------+------------+
| 语言      | languageid |
+===========+============+
| C         | 0          |
+-----------+------------+
| C++       | 1          |
+-----------+------------+
| Java      | 3          |
+-----------+------------+
| Python    | 6          |
+-----------+------------+
| PHP       | 7          |
+-----------+------------+
| JavaScript| 16         |
+-----------+------------+
| Go        | 17         |
+-----------+------------+
| SQL       | 18         |
+-----------+------------+

题库中的问题提交之前地址栏中会存在问题id，例如问题“还原撕碎的字条，哄笑生气的毛毛”的id为6264( `https://buctoj.com/problem.php?id=6264` )

函数返回来自BUCTOJ的response


新建问题
--------------------------------

::

    from BUCTOJ import create1problem, login
    cookies = login(管理员用户名, 管理员密码)
    problem_id = create1problem(cookies=cookies, title="题目标题", description="题目描述", input="输入描述", output="输出描述", sample_input="1\n0", sample_output="0")

上述代码会使用管理员账号创建一道新的问题，并返回新建问题的id。

在BUCTOJ提供的新建题目的网页经常会出现编辑了很多之后提交失败的情况，使用此脚本提交可以先在本地编辑好之后一次提交成功。

编辑问题
--------------------------------

::

    from BUCTOJ import edit1problem, login
    cookies = login(管理员用户名, 管理员密码)
    edit1problem(cookies=cookies, problem_id="6080", title=...后面参考新建问题create1problem函数)


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

下载某比赛/题目的所有提交/AC代码
--------------------------------

::

    from BUCTOJ import Config, login, saveAllCodes
    cookies = login('账号', '密码')
    saveAllCodes(baseurl='http://oj.narc.letmefly.xyz/status.php?cid=1269&jresult=4', cookies=cookies)

**前提**：

1. 拥有一个管理员账号

**功能**：

若满足以上一个条件，则此函数具有以下功能：

1. 获取baseurl的所有提交代码（会自动下一页）
2. 以“{用户}-{提交编号}.java”命名保存到results文件夹下（若无则会自动创建）

**TODO**：

1. 根据提交语音自动生成文件后缀，而非默认的.java
2. 支持用户自定义文件夹名，而非默认的results

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

TODO:
=============

BUGFIX: 脚本自动添加的头部会include上C++的 `<bits/stdc++.h>` 头文件，这可能导致原本能通过的代码产生编译错误（如 `int map;` 等）
