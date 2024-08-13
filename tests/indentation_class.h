// in

class Widget : public Base {
public:
void do_stuff();
private:
int m_member;
};

// out

class Widget : public Base {
public:
    void do_stuff();

private:
    int m_member;
};
