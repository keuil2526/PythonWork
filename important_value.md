| Column      | Meaning                           | Importance               |
| ----------- | --------------------------------- | ------------------------ |
| Survived    | Survive(Label)                    | ★★★★★                |
| Pclass      | Parlor class                      | ★★★★★                |
| Name        | Name                              | ★★★☆☆ (Extract Call) |
| gender      | Sex                               | ★★★★★                |
| Age         | Age                               | ★★★★★                |
| SibSp       | Number of siblings and spouses    | ★★★☆☆                |
| Parch       | Number of parents and children    | ★★★☆☆                |
| Ticket      | Ticket number                     | ★★☆☆☆                |
| Fare        | Fare                              | ★★★★☆                |
| Cabin       | Cabin                             | ★★★☆☆ (process)      |
| Embarked    | Embarked                          | ★★★☆☆                |
| boat        | Boat                              | ★☆☆☆☆                |
| body        | Body number                       | ★☆☆☆☆                |
| home.dest   | destination                       | ★☆☆☆☆                |


Name        No Need
Ticket      No Pattern
Cabin       Too Much Missing
Home Dest   Too Much Type
Boat        Data Leakage
Body        Data Leakage