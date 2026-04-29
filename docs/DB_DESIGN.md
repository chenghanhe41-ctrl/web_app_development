# 任務管理系統資料庫設計

## 1. 資料庫概述

本系統使用 SQLite 儲存任務資料。由於任務管理系統的資料結構較簡單，因此本次 MVP 只需要一個 tasks 資料表。

## 2. ER 圖

`mermaid
erDiagram
    TASKS {
        INTEGER id PK
        TEXT title
        TEXT description
        INTEGER is_completed
        TEXT created_at
        TEXT updated_at
    }
