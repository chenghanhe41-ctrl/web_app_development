# 任務管理系統架構設計

## 1. 系統概述

本系統採用 Flask、Jinja2 與 SQLite 建立一個簡單的任務管理 Web 應用程式。使用者可以透過瀏覽器操作任務資料，包括新增、查看、編輯、刪除與標記完成狀態。

## 2. 技術架構

- Flask：負責後端路由、請求處理與應用程式邏輯。
- Jinja2：負責 HTML 模板渲染，將後端資料顯示到網頁。
- SQLite：負責儲存任務資料。
- HTML/CSS：負責網頁結構與基本樣式。

## 3. 資料夾結構

task_manager_web/
├── app/
│   ├── __init__.py
│   ├── routes/
│   │   └── task_routes.py
│   ├── models/
│   │   └── task.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── create_task.html
│   │   └── edit_task.html
│   └── static/
│       └── style.css
├── database/
│   └── schema.sql
├── docs/
│   ├── PRD.md
│   └── ARCHITECTURE.md
├── run.py
└── README.md

## 4. MVC 架構說明

### Model

Model 負責資料結構與資料庫操作，例如任務的新增、查詢、更新、刪除。

位置：app/models/

### View

View 負責顯示 HTML 頁面，透過 Jinja2 將資料渲染到前端。

位置：app/templates/

### Controller

Controller 負責處理使用者請求、呼叫 Model、回傳 View。

位置：app/routes/

## 5. 系統運作流程

1. 使用者透過瀏覽器進入系統。
2. Flask 接收使用者的 HTTP 請求。
3. Route 根據請求呼叫對應的 Model。
4. Model 與 SQLite 資料庫互動。
5. Flask 將資料傳給 Jinja2 模板。
6. Jinja2 產生 HTML 頁面並回傳給使用者。

## 6. Flask、Jinja2、SQLite 協作方式

使用者在瀏覽器送出請求後，Flask Route 會接收請求並執行對應邏輯。如果需要讀取或修改資料，Route 會呼叫 Model，Model 再與 SQLite 資料庫互動。取得資料後，Flask 會將資料傳入 Jinja2 模板，最後由模板產生 HTML 頁面回傳給使用者。
