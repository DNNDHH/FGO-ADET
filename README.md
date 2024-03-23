# FGO-ADET
- FGO Account Decryption&amp;Encryption Tool (FGO 账号文件 解密&amp;加密 工具)
<img width="35%" style="border: 1px solid black" src="https://i.imgur.com/Bb5iUlu.png">

# 提取 游戏账号数据

需要提取账号数据才能执行此操作。
很简单，您所需要做的就是用文件管理器到以下路径并获取以下文件（可能需要ROOT）： 

| 版本 | 文件路径 | 文件名称 |
| --- | --- | --- | 
| JP | `android/data/com.aniplex.fategrandorder/files/data/` | 54cc790bf952ea710ed7e8be08049531 |

# 解密😍
- 用 记事本 或 文本编辑器 打开文件并从 ZSv开始复制到结束！(ZSv前面有一个什么坤八符号…不用复制它)
- 将复制的内容填写到 key_o.txt 之中！
- 运行 FGO-ADET 点击解密

# 加密😎
- 将你需要加密的 账户密钥 对应的填写 到 key_o.json 文件中 的 userId authKey secretKey 位置！
- 不要 删除或修改 文件中的 其它符号！
- 2018年之前的账户使用 加密模式o
- 2018年之后的账户使用 加密模式s
- 也不一定...建议 两个模式都试一试
- 运行 FGO-ADET 点击 加密模式 o 或 s
- 加密完成 将出现 54cc790bf952ea710ed7e8be08049531.txt 文件！

# 如何处理 加密回来的账号文件 让 FGO官方游戏客户端 可以登录使用😈

- 使用任意16进制编辑器打开 54cc790bf952ea710ed7e8be08049531.txt 文件，

在 5A 53 76 前面 插入 
```console
F8 01
  ```

使它变成
```console
F8 01 5A 53 76 
  ```
- 修改后的 54cc790bf952ea710ed7e8be08049531.txt 文件 删除 .txt 后缀名 并 复制两份 ，其中一份 重命名 为 969b46577f365fadeb79ef14cf5d6370
- 复制 54cc790bf952ea710ed7e8be08049531 和 969b46577f365fadeb79ef14cf5d6370 两个文件到 android/data/com.aniplex.fategrandorder/files/data/目录下！
- 这时候 FGO官方游戏客户端 就可以使用这个 账户文件 登录游戏了！

















