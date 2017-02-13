py_library(
    name = "custom_test_cases",
    srcs = ["custom_test_cases.py"]
)

py_test(
    name = "bubble_sort_test",
    srcs = ["bubble_sort_test.py"],
    deps = [
        ":custom_test_cases",
        "//python/sorting:bubble_sort",
    ],
)
