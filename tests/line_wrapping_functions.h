// in

ImportantClass::important_method(exc, limit, lookup_lines, capture_locals, extra_argument);

int long_function_signature(int first_param, float second_param, double third_param, bool flag) {
    return 0;
}

int very_long_function_signature(int first_param, float second_param, double third_param, const std::vector<int>& numbers) {
    return 1;
}

// out

ImportantClass::important_method(
    exc, limit, lookup_lines, capture_locals, extra_argument
);

int long_function_signature(
    int first_param, float second_param, double third_param, bool flag
) {
    return 0;
}

int very_long_function_signature(
    int first_param,
    float second_param,
    double third_param,
    const std::vector<int>& numbers
) {
    return 1;
}
