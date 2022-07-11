# GUI api

Repository description here

## Endpoints
- Users endpoints

|         |  metod  |                     endpoint                     |
|---------|---------|--------------------------------------------------|
| &check; |`GET`    |`/users`                                          |
| &check; |`GET`    |`/users/{user_id}`                                |
| &check; |`GET`    |`/users/{user_id}/permissions`                    |
| &check; |`GET`    |`/users/{user_id}/processes`                      |
| &check; |`GET`    |`/users/{user_id}/products`                       |
| &check; |`GET`    |`/users/{user_id}/actions`                        |
|         |`POST`   |`/users`                                          |
|         |`PATCH`  |`/users/{user_id}`                                |
|         |`DELETE` |`/users/{user_id}`                                |

- Processes endpoints

|         |  metod  |                     endpoint                     |
|---------|---------|--------------------------------------------------|
| &check; |`GET`    |`/processes`                                      |
| &check; |`GET`    |`/processes/{process_id}`                         |
| &check; |`GET`    |`/processes/{process_id}/reports`                 |
| &check; |`GET`    |`/processes/{process_id}/cards`                   |
| &check; |`GET`    |`/processes/{process_id}/cards/{card_id}`         |
| &check; |`GET`    |`/processes/{process_id}/cards/{card_id}/details` |
| &check; |`GET`    |`/processes/{process_id}/cards/{card_id}/logs`    |
|         |`POST`   |`/processes`                                      |
|         |`POST`   |`/processes/{process_id}/cards`                   |
|         |`POST`   |`/processes/{process_id}/logs`                    |
|         |`PATCH`  |`/processes/{process_id}`                         |
|         |`PATCH`  |`/processes/{process_id}/cards/{card_id}`         |
|         |`PATCH`  |`/processes/{process_id}/details/{card_id}`       |
|         |`PATCH`  |`/processes/{process_id}/logs/{log_id}`           |
|         |`DELETE` |`/processes/{process_id}`                         |
|         |`DELETE` |`/processes/{process_id}/logs/{log_id}`           |


- Products endpoints

|         |  metod  |                     endpoint                     |
|---------|---------|--------------------------------------------------|
| &check; |`GET`    |`/products`                                       |
| &check; |`GET`    |`/products/{product_id}`                          |
|         |`POST`   |`/products`                                       |
|         |`PATCH`  |`/products/{product_id}`                          |
|         |`DELETE` |`/products/{product_id}`                          |

- Permissions endpoints

|         |  metod  |                     endpoint                     |
|---------|---------|--------------------------------------------------|
|         |`GET`    |`/permissions`                                    |
|         |`GET`    |`/permissions/{permission_id}`                    |
|         |`POST`   |`/permissions`                                    |
|         |`PATCH`  |`/permissions/{permission_id}`                    |
|         |`DELETE` |`/permissions/{permission_id}`                    |

- Actions endpoints

|         |  metod  |                     endpoint                     |
|---------|---------|--------------------------------------------------|
|         |`GET`    |`/actions`                                        |
|         |`GET`    |`/actions/{action_id}`                            |
|         |`POST`   |`/actions`                                        |
|         |`PATCH`  |`/actions/{action_id}`                            |
|         |`DELETE` |`/actions/{action_id}`                            |

- Reports endpoints

|         |  metod  |                     endpoint                     |
|---------|---------|--------------------------------------------------|
|         |`GET`    |`/reports`                                        |
|         |`GET`    |`/reports/{report_id}`                            |
|         |`POST`   |`/reports`                                        |
|         |`PATCH`  |`/reports/{report_id}`                            |
|         |`DELETE` |`/reports/{report_id}`                            |

