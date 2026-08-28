# 🌐 Multilingual 5L System

**My World** features a robust, zero-fallback localization architecture across **5 global languages**:

---

## 1. Supported Languages

| Code | Language | Native Name | Script Type | Text Direction |
| :---: | :--- | :--- | :--- | :---: |
| `en` | English | English | Latin | LTR |
| `es` | Spanish | Español | Latin | LTR |
| `ja` | Japanese | 日本語 | Kanji / Katakana / Hiragana | LTR |
| `zh` | Chinese | 中文 | Simplified Chinese (Hanzi) | LTR |
| `ar` | Arabic | العربية | Arabic Script | **RTL** |

---

## 2. Zero-Fallback Localization Standard

In many multilingual web games, non-English languages frequently fall back to English words or mixed sentences. In **My World**, every data entity maintains 100% complete native sentences:

```json
{
  "es": "¿Sabías que La Paz (Bolivia) es la sede de gobierno más alta del planeta?",
  "en": "Did you know that La Paz (Bolivia) is the highest seat of government on Earth?",
  "ja": "ボリビアのラパスは標高3,640メートル以上に位置し、世界で最も高い政府所在地であることを知っていましたか？",
  "zh": "你知道玻利维亚的拉巴斯是地球上海拔最高的政府所在地吗？",
  "ar": "هل تعلم أن لا باز (بوليفيا) هي أعلى مقر حكومي على وجه الأرض وتقع على ارتفاع يتجاوز 3640 متراً؟"
}
```

---

## 3. Right-to-Left (RTL) Arabic Support

When Arabic (`ar`) is selected:
- The UI container dynamically applies `dir="rtl"` and adjusts layout alignment.
- Buttons, badge icons, and teletype messages format naturally according to Arabic typographic norms.
- Numbers and punctuation conform to modern standard Arabic presentation.\n