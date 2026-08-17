<img align='right' src="https://gifdb.com/images/high/hard-work-hardworking-cute-sticker-typing-2g9uumun7gfuzt3f.webp" width="200">
<h2> Hi, I'm Bao Nguyen <br>
A React Native Developer <img src="https://i.gifer.com/ZMQt.gif" width="50"></h2>

[![](https://img.shields.io/badge/Facebook-giaBaoJS-blue)](https://www.facebook.com/giaBaoJS)
[![](https://img.shields.io/badge/Instagram-paulnguyen249-E4405F)](https://www.instagram.com/paulnguyen249/)
[![](https://img.shields.io/badge/Gmail-giabaofrontend%40gmail.com-red)](mailto:giabaofrontend@gmail.com)
[![](https://img.shields.io/badge/GitHub-giaBaoJS-black)](https://github.com/giaBaoJS)

### <img src="https://i.pinimg.com/originals/63/b4/f2/63b4f20141bda26594b08fca821d6e4d.gif" width="50"> A little more about me...  

🚀 I'm a React Native Developer with 6+ years of experience in building high-quality and performant mobile applications  
💡 I'm passionate about creating impressive user experiences and writing clean, efficient code  
🔧 I publish native modules for React Native and fix bugs in the libraries I ship with  
📱 I love turning ideas into beautiful, functional mobile applications  
🐕 I absolutely love dogs and I'm a proud owner of 5 adorable poodles! They're my coding companions and stress relievers 

```javascript
const BaoInformation = {
    pronouns: "He" | "Him",
    askMeAbout: ["React Native Development", "Native Modules", "Mobile App Architecture", "UI/UX Design"],
    technologies: {
        frontend: ["React Native", "React", "TypeScript", "JavaScript"],
        native: ["Swift", "SwiftUI", "Objective-C", "Kotlin", "TurboModules", "Fabric"],
        backend: ["Node.js", "Express"],
        database: ["MongoDB", "MySQL", "Firebase"],
        tools: ["Expo", "React Native CLI", "Redux", "Context API", "TanStack"],
        design: ["Figma", "Adobe XD"],
        others: ["Git", "GitHub", "GitLab", "Bitbucket", "Jira", "VS Code", "Xcode", "Android Studio"]
    },
    currentFocus: "Open source native modules for the New Architecture",
    funFact: "I debug with console.log and I'm not ashamed! 😄",
    personalLife: "Dog lover with 5 poodles 🐩 - they're the best debugging partners!"
}
```

## <img src="https://i.gifer.com/WiqN.gif" width="50"> My Tech Stack 

### Mobile Development
![React Native](https://img.shields.io/badge/React_Native-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Expo](https://img.shields.io/badge/Expo-1B1F23?style=for-the-badge&logo=expo&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

### Native
![Swift](https://img.shields.io/badge/Swift-FA7343?style=for-the-badge&logo=swift&logoColor=white)
![SwiftUI](https://img.shields.io/badge/SwiftUI-0071E3?style=for-the-badge&logo=swift&logoColor=white)
![Kotlin](https://img.shields.io/badge/Kotlin-7F52FF?style=for-the-badge&logo=kotlin&logoColor=white)
![C++](https://img.shields.io/badge/C%2B%2B-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white)

### State Management & APIs
![Redux](https://img.shields.io/badge/Redux-593D88?style=for-the-badge&logo=redux&logoColor=white)
![React Query](https://img.shields.io/badge/React_Query-FF4154?style=for-the-badge&logo=react%20query&logoColor=white)
![Axios](https://img.shields.io/badge/Axios-5A29E4?style=for-the-badge&logo=axios&logoColor=white)

### Development Tools
![VS Code](https://img.shields.io/badge/VS_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)
![Xcode](https://img.shields.io/badge/Xcode-007ACC?style=for-the-badge&logo=Xcode&logoColor=white)
![Android Studio](https://img.shields.io/badge/Android_Studio-3DDC84?style=for-the-badge&logo=android-studio&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

## <img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExbG1wcmNnd3lhYWNrOGMyNnA4OTBhcGhtZGdlYzd3cGExd3M1YmNkeCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/C3NZtLRo8TMHvVCFFE/giphy.gif" width="50"> Open Source Contributions

**27 pull requests to 6 projects.** I use these libraries in production, so when something breaks I go and fix it upstream — every PR below comes with a root-cause write-up and a regression test.

<br>

### [Shopify/react-native-skia](https://github.com/Shopify/react-native-skia) [![stars](https://img.shields.io/github/stars/Shopify/react-native-skia?style=flat-square&label=%E2%AD%90&labelColor=161B22&color=1F6FEB)](https://github.com/Shopify/react-native-skia)
<sub>High-performance 2D graphics for React Native</sub>

| PR | What it fixes |
| :-- | :-- |
| [#4001](https://github.com/Shopify/react-native-skia/pull/4001) `open` | **Use-after-free in `Font.getTypeface()`.** The borrowed pointer from `SkFont::getTypeface()` was adopted into an owning `sk_sp` without a ref, so every call silently drained the typeface's refcount until it was destroyed underneath live fonts. Proven with a C++ harness linked against the real prebuilt Skia binary — the unpatched build `SIGABRT`s, the patched one exits clean. |

<br>

### [nguyenphutrong/quotio](https://github.com/nguyenphutrong/quotio) [![stars](https://img.shields.io/github/stars/nguyenphutrong/quotio?style=flat-square&label=%E2%AD%90&labelColor=161B22&color=1F6FEB)](https://github.com/nguyenphutrong/quotio)
<sub>Native macOS menu bar app that unifies your AI subscriptions — Swift 6, strict concurrency</sub>

| PR | What it fixes |
| :-- | :-- |
| [#467](https://github.com/nguyenphutrong/quotio/pull/467) `open` | Configuring the proxy overwrote `~/.codex/auth.json` wholesale, destroying credentials — now a merge-write with a restorable backup |
| [#471](https://github.com/nguyenphutrong/quotio/pull/471) `open` | Round-tripping an auth file dropped every field the app didn't recognise — silent data loss straight into the Keychain |
| [#477](https://github.com/nguyenphutrong/quotio/pull/477) `open` | An `opencode.json` with comments failed to parse and got wiped; now parses JSONC and splices a single field back byte-for-byte |
| [#481](https://github.com/nguyenphutrong/quotio/pull/481) `open` | Custom HTTP headers for custom providers, with RFC 7230 validation so a CR/LF in a header value can't inject a request |
| [#475](https://github.com/nguyenphutrong/quotio/pull/475) `open` | A `-1` "no data" sentinel was rendered as `100 − (−1)` = **101%** — placeholder now, in the ring and in VoiceOver |
| [#472](https://github.com/nguyenphutrong/quotio/pull/472) `open` | Accounts imported from Cursor and Trae couldn't be deleted — and deleted ones resurrected on the next scan |

<details>
<summary><b>15 more →</b></summary>

<br>

| PR | What it does |
| :-- | :-- |
| [#468](https://github.com/nguyenphutrong/quotio/pull/468) `open` | Classify Codex quota windows by actual duration instead of position in the response |
| [#469](https://github.com/nguyenphutrong/quotio/pull/469) `open` | Deduplicate Copilot quota items appearing twice under legacy and current identity keys |
| [#470](https://github.com/nguyenphutrong/quotio/pull/470) `open` | Show the provider in the request log — and stop attributing Kiro requests to Claude |
| [#473](https://github.com/nguyenphutrong/quotio/pull/473) `open` | Configurable reasoning effort for Codex models |
| [#474](https://github.com/nguyenphutrong/quotio/pull/474) `open` | Let the user choose which quota bucket the menu bar shows |
| [#476](https://github.com/nguyenphutrong/quotio/pull/476) `open` | Complete app reset in Settings, with an injectable directory so tests never touch real data |
| [#478](https://github.com/nguyenphutrong/quotio/pull/478) `open` | Sort the accounts currently in use to the top of the menu |
| [#479](https://github.com/nguyenphutrong/quotio/pull/479) `open` | Detect Trae CN in "Scan for IDEs", with a domain allowlist so a user-writable file can't exfiltrate a token |
| [#480](https://github.com/nguyenphutrong/quotio/pull/480) `open` | Persist traffic statistics across proxy restarts, with a versioned store and migration |
| [#482](https://github.com/nguyenphutrong/quotio/pull/482) `open` | Split Gemini models into their own Google-protocol provider for OpenCode |
| [#483](https://github.com/nguyenphutrong/quotio/pull/483) `open` | Show available models in the app panel, distinguishing "empty" from "failed to load" |
| [#484](https://github.com/nguyenphutrong/quotio/pull/484) `open` | Opt-in restore of agent configs on quit, keyed by a SHA-256 receipt so it never clobbers a config it didn't write |
| [#485](https://github.com/nguyenphutrong/quotio/pull/485) `open` | Carry explicit quota bucket kinds from the fetchers instead of inferring them from display strings |
| [#486](https://github.com/nguyenphutrong/quotio/pull/486) `open` | Refresh imported Cursor and Trae quotas on a global refresh |
| [#487](https://github.com/nguyenphutrong/quotio/pull/487) `open` | Opt-in adaptive refresh cadence that backs off when nothing is changing |

</details>

<br>

### [heroui-inc/heroui-native](https://github.com/heroui-inc/heroui-native) [![stars](https://img.shields.io/github/stars/heroui-inc/heroui-native?style=flat-square&label=%E2%AD%90&labelColor=161B22&color=1F6FEB)](https://github.com/heroui-inc/heroui-native)
<sub>Beautiful, fast and modern React Native UI library</sub>

| PR | What it fixes |
| :-- | :-- |
| [#464](https://github.com/heroui-inc/heroui-native/pull/464) `open` | **`<Typography weight>` stopped working in v1.0.6.** The BEM migration dropped the font-weight declarations, so every weight rendered identically unless you defined custom font variables. Traced to the exact migration PR that introduced it. |

<br>

### [gronxb/hot-updater](https://github.com/gronxb/hot-updater) [![stars](https://img.shields.io/github/stars/gronxb/hot-updater?style=flat-square&label=%E2%AD%90&labelColor=161B22&color=1F6FEB)](https://github.com/gronxb/hot-updater)
<sub>Self-hostable OTA update solution for React Native</sub>

| PR | What it does |
| :-- | :-- |
| [#1142](https://github.com/gronxb/hot-updater/pull/1142) `merged` ✅ | **New `@hot-updater/bugsnag-plugin`** — uploads source maps to BugSnag on every release so crash reports from OTA bundles are readable |
| [#1143](https://github.com/gronxb/hot-updater/pull/1143) `open` | An unknown built-in baseline bundle id was treated as a real baseline, so devices could be handed an update they couldn't apply |

<br>

### [margelo/react-native-filament](https://github.com/margelo/react-native-filament) [![stars](https://img.shields.io/github/stars/margelo/react-native-filament?style=flat-square&label=%E2%AD%90&labelColor=161B22&color=1F6FEB)](https://github.com/margelo/react-native-filament)
<sub>Google's Filament 3D renderer for React Native</sub>

| PR | What it fixes |
| :-- | :-- |
| [#345](https://github.com/margelo/react-native-filament/pull/345) `open` | **`file://` URIs were never percent-decoded**, so any asset with a space or a non-ASCII character in its path failed to load on both platforms. Guarded so an existing file with a literal `%` in its name doesn't regress. |

<br>

### [software-mansion-labs/react-native-bottom-sheet](https://github.com/software-mansion-labs/react-native-bottom-sheet) [![stars](https://img.shields.io/github/stars/software-mansion-labs/react-native-bottom-sheet?style=flat-square&label=%E2%AD%90&labelColor=161B22&color=1F6FEB)](https://github.com/software-mansion-labs/react-native-bottom-sheet)
<sub>Bottom sheet components for React Native</sub>

| PR | What it fixes |
| :-- | :-- |
| [#71](https://github.com/software-mansion-labs/react-native-bottom-sheet/pull/71) `open` | **Nested scrollables were hit-tested from the wrong point on iOS** — the post-threshold pan location instead of the touch-down point, so a gesture that started inside an inner list could be stolen by the sheet |

<br>

## <img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExNzdkbml6cjAxN2p1dzhtNTI5N3VrYTJzN2hhc3JrNDY1YWljb2xueiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/hDLiT6bW6E74jLu3Gw/giphy.gif" width="50"> Libraries I've Published

Native modules for the New Architecture, plus one SwiftUI package. All MIT, all with example apps and CI.

| Library | What it does | |
| :-- | :-- | :-- |
| **[react-native-device-pulse](https://github.com/giaBaoJS/react-native-device-pulse)** | Device health from JS — thermal state, low power mode, memory warnings. Event listeners and React hooks. | [![npm](https://img.shields.io/npm/v/react-native-device-pulse?style=flat-square&labelColor=161B22&color=CB3837&logo=npm&logoColor=white)](https://www.npmjs.com/package/react-native-device-pulse) |
| **[react-native-app-shortcuts](https://github.com/giaBaoJS/react-native-app-shortcuts)** | Home screen quick actions — `UIApplicationShortcutItem` on iOS, `ShortcutManager` on Android. | [![npm](https://img.shields.io/npm/v/%40giabaojs%2Freact-native-app-shortcuts?style=flat-square&labelColor=161B22&color=CB3837&logo=npm&logoColor=white)](https://www.npmjs.com/package/@giabaojs/react-native-app-shortcuts) |
| **[react-native-shared-transition](https://github.com/giaBaoJS/react-native-shared-transition)** | Shared element transitions between screens. Revived and rewritten — first working iOS build in the project's history. | [![npm](https://img.shields.io/npm/v/react-native-shared-transition?style=flat-square&labelColor=161B22&color=CB3837&logo=npm&logoColor=white)](https://www.npmjs.com/package/react-native-shared-transition) |
| **[react-native-tipkit](https://github.com/giaBaoJS/react-native-tipkit)** | Apple's TipKit for React Native — popover and inline tips, display rules, event counts, frequency control. | [![npm](https://img.shields.io/npm/v/%40giabaojs%2Freact-native-tipkit?style=flat-square&labelColor=161B22&color=CB3837&logo=npm&logoColor=white)](https://www.npmjs.com/package/@giabaojs/react-native-tipkit) |
| **[react-native-image-analysis](https://github.com/giaBaoJS/react-native-image-analysis)** | On-device OCR with text geometry, barcodes, and a tap-to-select text view. Apple VisionKit on iOS, Google ML Kit on Android. | |
| **[react-native-ios-controls](https://github.com/giaBaoJS/react-native-ios-controls)** | Control Center, Lock Screen and Action Button controls (iOS 18 `ControlWidget`), plus a CLI that wires up the widget target for you. | |
| **[ToastKit](https://github.com/giaBaoJS/ToastKit)** | A polished SwiftUI toast & snackbar library — queued toasts, semantic styles, swipe-to-dismiss, full accessibility. | [![docs](https://img.shields.io/badge/DocC-docs-orange?style=flat-square&labelColor=161B22&logo=swift&logoColor=white)](https://giabaojs.github.io/ToastKit/documentation/toastkit/) |

## <img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHVnZXh3ZG1qaXQ5ejI0YzQ4Mm5qN2s2cXcweWVzMTA1aGdjYm92ZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/ShM3DqhMzYxQPaT2qQ/giphy.gif" width="50"> Activity Graph
<img src="https://github-readme-activity-graph.vercel.app/graph?username=giaBaoJS&theme=tokyo-night&hide_border=true" />

<img src="https://media.giphy.com/media/LnQjpWaON8nhr21vNW/giphy.gif" width="60"> <em><b>I love connecting with different people</b> so if you want to say <b>hi, I'll be happy to meet you more!</b> 😊</em>

---
<div align="center">
  <img src="https://komarev.com/ghpvc/?username=giaBaoJS&color=blueviolet&style=flat-square&label=Profile+Views" />
</div>
