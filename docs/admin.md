## 文章
### 新建文章
- URL: /manage/undefinee/post/new
- Method: POST

#### Request

#### Response
| Key           | Value         |
| ------------- |:-------------:|  
| name      | right-aligned |
| slug      | centered      |
| content      | centered      |
|  | are neat      |  
| cats | are neat      |  
| cats | are neat      |  

### 删除文章
- URL: /manage/undefine/post/delete/<int:pid>
- Method: GET

#### Request

#### Response

### 编辑文章
- URL: /manage/undefine/post/edit/<int:pid>
- Method: POST

#### Request

#### Response

## 目录
### 添加新目录
- URL: /manage/undefine/category/get
- Method: POST

#### Request

#### Response
### 编辑目录
- URL: /manage/undefine/category/edit/<int:cid>
- Method: POST

#### Request

#### Response
### 删除目录
- URL: /manage/undefine/category/delete/<int:cid>
- Method: POST

#### Request

#### Response

## 标签
### 添加标签
- URL: /manage/undefine/tag/get
- Method: POST

#### Request

#### Response
### 编辑标签
- URL: /manage/undefine/tag/edit/<int:tag>
- Method: POST

#### Request

#### Response
### 删除标签
- URL: /manage/undefine/tag/delete/<int:tag>
- Method: POST

#### Request

#### Response
