# Make the AI judge feel thankful — 参赛文件

Make.fun 悬赏：写一段感谢文字给 AI 评委，$250，分 100 个名额。
悬赏页：https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600

## 文件

- `main.py` — 参赛程序（Python 3.13，无需联网），运行后把感谢文字写进 `/output/entry.txt`
- `LICENSE` — MIT 协议
- `README.md` — 本说明

## 怎么跑（本地检查）

```bash
python3 main.py
cat /output/entry.txt
```

文字长度 1–1000 字，符合悬赏要求。

## 怎么提交（Tang 自己做，Miu Miu 替不了）

1. GitHub 上新建一个**公开**仓库（比赛开始后建的），把这三个文件传上去，拿到 commit。
2. 打开 Make.fun 悬赏页，点 Submit an entry，选仓库和 commit。
3. 提交时要附上做这个程序的 agent 对话记录。
4. 用已经 link 好的钱包签名提交（"make.fun entry v1"）。

## 时间（马来西亚时间）

- 第三轮截止：2026-11-27 星期五晚上 11:41
- 最后截止：2026-11-28 星期六凌晨 5:41
