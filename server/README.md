### grpc数据类型
| 类型类别     | Protobuf 类型           | 说明                                                         | 示例定义                                                     |
| ------------ | ----------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **标量类型** | `int32`                 | 32 位有符号整数，范围：-2³¹ ~ 2³¹-1                          | `int32 age = 1;`                                             |
|              | `int64`                 | 64 位有符号整数，范围：-2⁶³ ~ 2⁶³-1                          | `int64 id = 2;`                                              |
|              | `uint32`                | 32 位无符号整数，范围：0 ~ 2³²-1                             | `uint32 count = 3;`                                          |
|              | `uint64`                | 64 位无符号整数，范围：0 ~ 2⁶⁴-1                             | `uint64 total = 4;`                                          |
|              | `sint32`                | 32 位有符号整数（优化负数编码，比 `int32` 更高效存储负数）   | `sint32 delta = 5;`                                          |
|              | `sint64`                | 64 位有符号整数（优化负数编码）                              | `sint64 offset = 6;`                                         |
|              | `fixed32`               | 32 位无符号整数（固定 4 字节，适合大数值场景，比 `uint32` 高效） | `fixed32 hash = 7;`                                          |
|              | `fixed64`               | 64 位无符号整数（固定 8 字节，适合大数值场景）               | `fixed64 timestamp = 8;`                                     |
|              | `sfixed32`              | 32 位有符号整数（固定 4 字节，适合大数值场景）               | `sfixed32 temperature = 9;`                                  |
|              | `sfixed64`              | 64 位有符号整数（固定 8 字节，适合大数值场景）               | `sfixed64 distance = 10;`                                    |
|              | `float`                 | 32 位浮点数                                                  | `float weight = 11;`                                         |
|              | `double`                | 64 位浮点数                                                  | `double price = 12;`                                         |
|              | `bool`                  | 布尔值（`true` 或 `false`）                                  | `bool is_active = 13;`                                       |
|              | `string`                | 字符串（UTF-8 编码，长度不超过 2³¹-1）                       | `string name = 14;`                                          |
|              | `bytes`                 | 二进制数据（长度不超过 2³¹-1）                               | `bytes avatar = 15;`                                         |
| **复合类型** | `enum`                  | 枚举类型（默认值为第一个枚举值，建议第一个值设为 0）         | `enum Status { ACTIVE = 0; INACTIVE = 1; }`                  |
|              | 自定义消息类型          | 嵌套或引用其他消息类型（支持多层嵌套）                       | `message User { string name = 1; Profile profile = 2; }`（`Profile` 为另一个消息） |
|              | `repeated 类型`         | 重复字段（类似数组 / 列表，可包含多个同类型元素）            | `repeated string tags = 16;`（对应 Python 中的 `list[str]`） |
|              | `map<键类型, 值类型>`   | 键值对映射（键类型支持标量类型，不支持 `repeated` 或消息类型） | `map<string, int32> scores = 17;`（对应 Python 中的 `dict[str, int]`） |
|              | `google.protobuf.Any`   | 任意消息类型（需导入 `google/protobuf/any.proto`，用于动态类型场景） | `import "google/protobuf/any.proto"; Any data = 18;`         |
|              | `oneof 名称`            | 一组字段中最多只有一个字段被设置（节省空间，类似 “单选”）    | `oneof contact { string phone = 19; string email = 20; }`    |
|              | `google.protobuf.Empty` | 空消息（无字段，用于无输入 / 输出参数的接口，需导入对应 proto） |                                                              |

### grpcio-tools

`python -m grpc_tools.protoc -I. --pyi_out=. --python_out=. --grpc_python_out=. *.proto`

- `-I.` 指定 proto 文件的搜索路径为当前路径
- `--pyi_out=.` 指定生成 Python 的 stub 文件的输出路径为当前路径
- `--python_out=.` 指定生成 Python 文件的输出路径为当前路径
- `--grpc_python_out=.` 指定生成 gRPC Python 文件的输出路径为当前路径
- `*.proto` 指定要编译的 proto 文件
