// in

auto result = std::optional<int>(123)
                  .transform([](int n) { return n + 100; })
                  .transform([](int n) {
                      // multiline lambda
                      return std::to_string(n);
                  });

// out

auto result = std::optional<int>(123)
    .transform([](int n) { return n + 100; })
    .transform([](int n) {
        // multiline lambda
        return std::to_string(n);
    });
