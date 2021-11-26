def arr_to_csv:
  .items as $items | 
  ["id", "created_at", "name", "has_test", "alternate_url"] as $keys | 
  reduce $items[] as $item ([]; . + 
    [ 
      reduce $keys[] as $key ([]; . + [$item[$key]]) | 
      @csv 
    ])|
    [$keys | @csv] + . | .[];

arr_to_csv