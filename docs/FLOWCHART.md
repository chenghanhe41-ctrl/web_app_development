# 任務管理系統流程圖設計

## 1. 使用者主要操作流程

```mermaid
flowchart TD
    Start([使用者進入系統])
    Home[顯示任務列表首頁]
    Choose{選擇操作}

    Create[新增任務]
    Edit[編輯任務]
    Delete[刪除任務]
    Toggle[切換完成狀態]
    Filter[篩選任務]

    SaveCreate[儲存新任務]
    SaveEdit[儲存修改]
    DoDelete[刪除資料]
    UpdateStatus[更新狀態]
    ShowFiltered[顯示篩選結果]

    Start --> Home
    Home --> Choose

    Choose --> Create
    Create --> SaveCreate
    SaveCreate --> Home

    Choose --> Edit
    Edit --> SaveEdit
    SaveEdit --> Home

    Choose --> Delete
    Delete --> DoDelete
    DoDelete --> Home

    Choose --> Toggle
    Toggle --> UpdateStatus
    UpdateStatus --> Home

    Choose --> Filter
    Filter --> ShowFiltered
    ShowFiltered --> Home
