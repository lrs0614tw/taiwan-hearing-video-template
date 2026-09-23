# Taiwan Hearing Video Template

供 Codex 使用的台灣立法院質詢影片與封面套版 Skill，支援：

- 1920 × 1080、16:9 橫式長影片
- 1080 × 1920、9:16 直式短影片
- 1920 × 1080 長影片封面

固定 PNG 只保存格線、斜線、圓形、星芒與字幕帶；日期、會議名稱、人物標籤、字幕、重點字卡與封面標題均保持動態。

## 素材

| 檔案 | 尺寸 | 用途 |
|---|---:|---|
| `assets/full-overlay.png` | 1920 × 1080 | 橫式影片完整透明套版 |
| `assets/header.png` | 1920 × 1080 | 橫式上方資訊欄 |
| `assets/subtitle-band.png` | 1920 × 1080 | 橫式下方字幕帶 |
| `assets/vertical-full-overlay.png` | 1080 × 1920 | 直式影片完整透明套版 |
| `assets/vertical-header.png` | 1080 × 1920 | 直式上方資訊欄 |
| `assets/vertical-subtitle-band.png` | 1080 × 1920 | 直式下方字幕帶 |
| `assets/cover-background.png` | 1920 × 1080 | 長影片封面背景 |

同一比例只能使用完整套版，或使用對應的上下分層素材，不可重複疊加。

## 字體

模板內附：

- `SweiMarkerLegCJKtc-Bold.ttf`：日期、會議名稱、人物標籤、一般字幕。
- `SweiMarkerLegCJKtc-Black.ttf`：較重的資訊文字、標籤與重點字卡。
- `MantouSans-Regular.ttf`：短封面標題或大型重點字卡。

渲染時直接指定 skill 內的字體檔，不使用 Noto Sans CJK TC 代替。兩套字體均採 SIL Open Font License 1.1，授權文件位於 `assets/fonts/`。

## 使用範例

```text
請使用 edit-youthful-social-video 和 taiwan-hearing-video-template，
輸出一支 16:9 橫式長版、三支 30–90 秒的 9:16 短版，以及一張 16:9 封面。
先讓我確認長版主軸與三支短片題目，再製作橫式及直式預覽。
```

## 版面規則

- 所有固定資產都以原尺寸放在 `(0, 0)`，不可拉伸或跨比例使用。
- 橫式與直式字幕帶都維持左低右高。
- 人物標籤只在身分確認且人物實際入鏡時顯示。
- 原始時間碼若不在不透明字幕帶後方，應另外裁切或覆蓋。
- 封面使用一個 6–12 字主標題、一個小型資訊區，最多再加一個議題標籤與短 Hashtag。
- 文字、描邊、陰影、旋轉角與裝飾完成後，都必須重新檢查完整繪製邊界。

詳細座標與圖層順序請見 [`references/layout-spec.md`](references/layout-spec.md)。

## 安裝

### macOS／Linux

```bash
git clone https://github.com/lrs0614tw/taiwan-hearing-video-template.git ~/.codex/skills/taiwan-hearing-video-template
```

### Windows PowerShell

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills" | Out-Null
git clone https://github.com/lrs0614tw/taiwan-hearing-video-template.git "$env:USERPROFILE\.codex\skills\taiwan-hearing-video-template"
```

安裝後重新啟動 Codex，或建立新的 Codex 工作。

## 維護

預建 PNG 已包含在 repository 中。若要重新產生直式與封面固定素材，可使用具備 Pillow 的 Python 執行：

```bash
python3 scripts/build_assets.py
```

重新產生後，必須檢查透明度、尺寸、字幕帶方向與所有裝飾是否完整。

## 專案結構

```text
.
├── README.md
├── SKILL.md
├── assets/
│   ├── fonts/
│   ├── cover-background.png
│   ├── full-overlay.png
│   ├── header.png
│   ├── subtitle-band.png
│   ├── vertical-full-overlay.png
│   ├── vertical-header.png
│   └── vertical-subtitle-band.png
├── references/
│   └── layout-spec.md
└── scripts/
    └── build_assets.py
```

## 安全提醒

公開或分享影片前，請確認來源影片、人物資訊、字幕、視覺素材與字體使用符合實際授權。
