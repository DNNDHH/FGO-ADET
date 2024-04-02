# FGO-ADET
- FGO Account Decryption&amp;Encryption Tool 
- FGO 账号文件 解密&amp;加密 工具
<img width="35%" style="border: 1px solid black" src="https://i.imgur.com/Bb5iUlu.png">

# 提取 游戏账号数据

需要提取账号数据才能执行此操作。
很简单，您所需要做的就是用文件管理器到以下路径并获取以下文件（可能需要ROOT）： 

| 版本 | 文件路径 | 文件名称 |
| --- | --- | --- | 
| JP | `android/data/com.aniplex.fategrandorder/files/data/` | 54cc790bf952ea710ed7e8be08049531 |

# 解密😍
- 复制 54cc790bf952ea710ed7e8be08049531 文件到 FGO-ADET 目录下
- 
- 运行 FGO-ADET.exe , 点击 Decrypt (解密)
- 
- 打开 Decrypt_Server_Key.json 就可以看到 userId authKey secretKey
- 
- 然后随便你怎么用 开挂发包 还是 自动登录签到


# 加密😎
- 将你需要加密的 账户密钥 对应的 填写 到 encrypt_o.json 或者 encrypt_s.json 文件中 的 userId authKey secretKey 三个对应的位置！
- 
- 不要 删除或修改 文件中的 其它符号！
- 
- 2018年之前的账户使用 加密模式 o (encrypt_o.json)
- 2018年之后的账户使用 加密模式 s (encrypt_s.json)
- 
- 也不一定...建议 两个模式都试一试😛lol
- 
- 运行 FGO-ADET.exe , 对应的点击  Encryption mode o（加密模式o） 或 Encryption mode s（加密模式s）
- 
- 加密完成的文件 将出现在当前目录中的 com.aniplex.fategrandorder 文件夹内 /files/data 目录之中！
- 
- 复制 54cc790bf952ea710ed7e8be08049531 和 969b46577f365fadeb79ef14cf5d6370 两个文件到 你的手机 或者 模拟器 中的 android/data/com.aniplex.fategrandorder/files/data/ 目录下！
- 
- 这时候 打开 FGO官方游戏客户端 就可以使用这个 账号文件 登录游戏了！

















