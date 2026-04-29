# 任務管理系統路由設計

## 1. 路由總覽

| 方法 | 路徑 | 功能 | 對應模板 |
|---|---|---|---|
| GET | / | 顯示任務列表首頁 | index.html |
| GET | /tasks/new | 顯示新增任務表單 | create_task.html |
| POST | /tasks/new | 新增任務資料 | 無，完成後重新導向首頁 |
| GET | /tasks/<id>/edit | 顯示編輯任務表單 | edit_task.html |
| POST | /tasks/<id>/edit | 更新任務資料 | 無，完成後重新導向首頁 |
| POST | /tasks/<id>/delete | 刪除任務 | 無，完成後重新導向首頁 |
| POST | /tasks/<id>/toggle | 切換任務完成狀態 | 無，完成後重新導向首頁 |

## 2. 頁面說明

### 首頁 /

首頁顯示所有任務，並提供新增、編輯、刪除、切換完成狀態與篩選功能。

### 新增任務 /tasks/new

提供表單讓使用者輸入任務標題與內容。

### 編輯任務 /tasks/<id>/edit

提供表單讓使用者修改指定任務。

## 3. 模板清單

- base.html：共用版型
- index.html：任務列表頁
- create_task.html：新增任務頁
- edit_task.html：編輯任務頁

## 4. 路由骨架說明

本階段只建立路由函式骨架，實際資料庫操作會在實作階段完成。
