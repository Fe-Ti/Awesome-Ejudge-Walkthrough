////////////////////////////////////////////////////////////////////////////////
//  Discipline: Algorithms and Data Structures (AaDS)
//  File: Module 1 Task B.
//  Copyright 2022 Fe-Ti <btm.007@mail.ru>
//    .-.
//   (   |.
//    '-=||=====-===\/===--.
//       ||        /||   o  '.
//       ||  .-.  / ||  /|   |
//     .=||=(--' /  || / |  ,'
//    (  ||  '--'   ||/  '-'
//     '-'
//
//  Description: Just a simple dequeue
//  License: BSD
////////////////////////////////////////////////////////////////////////////////

#include <iostream>
#include <string>
#include <vector>

struct StringDequeue {
    uint64_t _head = 0;
    uint64_t _tail = 0;
    uint64_t _allocated_size = 0;
    std::string* _data;
    bool is_empty = true;

    StringDequeue(uint64_t maxsize)
    {
        _allocated_size = maxsize;
        _data = new std::string[_allocated_size];
    }

    std::string pop(uint64_t index)
    {
        std::string element = _data[index];
        return element;
    }

    std::string popb()
    {
        if (head_tail_delta() == 0) {
            if (is_empty)
                throw "underflow";
            else
                is_empty = true;
        }
        std::string element = pop(_tail);
        if (!is_empty) {
            --_tail;
            if (_tail > _allocated_size) {
                _tail += _allocated_size;
            }
        }
        //                    std::cout << "New _head " << _head << std::endl;
        //                    std::cout << "And _tail " << _tail << std::endl;

        return element;
    }
    std::string popf()
    {
        if (head_tail_delta() == 0) {
            if (is_empty)
                throw "underflow";
            else
                is_empty = true;
        }
        std::string element = pop(_head);
        if (!is_empty) {
            _head = (++_head) % _allocated_size;
        }
        //                    std::cout << "New _head " << _head << std::endl;
        //                    std::cout << "And _tail " << _tail << std::endl;
        return element;
    }

    void push(uint64_t index, const std::string& element)
    {
        _data[index] = element;
    }

    void pushb(const std::string& element)
    {
        if (size() == _allocated_size) {
            throw "overflow";
        }
        if (is_empty) {
            is_empty = false;
        } else {
            _tail = (++_tail) % _allocated_size;
        }
        push(_tail, element);
        //                    std::cout << "New _tail " << _tail << std::endl;
        //                    std::cout << "And _head " << _head << std::endl;
    }
    void pushf(const std::string& element)
    {
        if (size() == _allocated_size) {
            throw "overflow";
        }
        if (is_empty) {
            is_empty = false;
        } else {
            --_head;
            if (_head > _allocated_size) {
                _head += _allocated_size;
            }
        }
        push(_head, element);
        //                    std::cout << "New _head " << _head << std::endl;
        //                    std::cout << "And _tail " << _tail << std::endl;
    }

    void print(const std::string& delim = " ")
    {
        if (head_tail_delta() == 0) {
            if (is_empty)
                std::cout << "empty" << std::endl;
            else
                std::cout << _data[_head] << std::endl;
        } else {
            for (uint64_t i = _head; i < (head_tail_delta() + _head); ++i) {
                std::cout << _data[(i) % _allocated_size] << delim;
                //                std::cout << _data[(i) % _allocated_size] <<
                //                "." << i << "."
                //                          << (i) % _allocated_size << "||";
            }
            std::cout << _data[(head_tail_delta() + _head) % _allocated_size]
                      << std::endl;
        }
    }

    uint64_t head_tail_delta()
    {
        uint64_t sz = (_tail - _head);
        if (sz > _allocated_size) {
            sz += _allocated_size;
        }
        return sz;
    }

    uint64_t size()
    {
        if (is_empty)
            return 0;
        else
            return (head_tail_delta() + 1);
    }

    ~StringDequeue() { delete[] _data; }
};

const char SPACE = ' ';
const char* ERROR = "error";
const char* INIT_DEQ = "set_size";
const char* PUSH_F = "pushf";
const char* PUSH_B = "pushb";
const char* POP_F = "popf";
const char* POP_B = "popb";
const char* PRINT = "print";
const char* INFO = "info";

void
operator<<(std::string& sl, std::string& sr)
{
    size_t count = 0;
    for (; count < sr.size(); ++count) {
        if (sr[count] == SPACE) {
            break;
        }
    }
    sl = sr.substr(0, count);
    for (; count < sr.size(); ++count) {
        if (sr[count] != SPACE) {
            break;
        }
    }
    if (count < sr.size())
        sr = sr.substr(count);
    else
        sr = "";
}

bool
isspace(const std::string& str)
{
    for (size_t i = 0; i < str.size(); ++i) {
        if (str[i] != SPACE)
            return false;
    }
    return true;
}
void
check_emptyness(const std::string& str)
{
    if ((!str.empty()) && !isspace(str)) {
        throw ERROR;
    }
}

int
main()
{
    std::string cmdline;
    std::string cmd;
    std::getline(std::cin, cmdline);
    StringDequeue* d_p;

    bool is_running_flag = false;
    while (!std::cin.eof()) {
        if (!cmdline.empty()) { // && !isspace(cmdline)) {
            //////////////////////////////////////////////
            //           !!! kludge thing !!!           //
            // Q: Why this is here?
            // A: For whatever reason we should consilder
            //    commands with space character at the end
            //    (like "print  ") as incorrect cmds.
            //
            if (cmdline[cmdline.size() - 1] == SPACE) {
                std::cout << ERROR << std::endl;
            }
            //                                          //
            //////////////////////////////////////////////
            else {
                cmd << cmdline;
                if (!is_running_flag) {
                    if (cmd == INIT_DEQ) {
                        try {
                            cmd << cmdline;
                            //                    int64_t dq_size =
                            //                    std::stoi(cmd); if (dq_size <
                            //                    0)
                            //                        throw ERROR;
                            d_p = new StringDequeue(std::stoi(cmd));
                            is_running_flag = true;
                        } catch (...) {
                            std::cout << ERROR << std::endl;
                        }
                    } else {
                        std::cout << ERROR << std::endl;
                    }
                } else {
                    try {
                        if (cmd == PUSH_F) {
                            cmd << cmdline;
                            check_emptyness(cmdline);
                            d_p->pushf(cmd);
                        } else if (cmd == PUSH_B) {
                            cmd << cmdline;
                            check_emptyness(cmdline);
                            d_p->pushb(cmd);
                        } else if (cmd == POP_F) {
                            check_emptyness(cmdline);
                            std::cout << d_p->popf() << std::endl;
                        } else if (cmd == POP_B) {
                            check_emptyness(cmdline);
                            std::cout << d_p->popb() << std::endl;
                        } else if (cmd == PRINT) {
                            check_emptyness(cmdline);
                            d_p->print();
                            //                } else if (cmd == INFO) {
                            //                    std::cout << "_head:" <<
                            //                    d_p->_head << std::endl;
                            //                    std::cout
                            //                    << "_tail:" << d_p->_tail <<
                            //                    std::endl; std::cout <<
                            //                    "_allocated_size:" <<
                            //                    d_p->_allocated_size
                            //                              << std::endl
                            //                              << "print():";
                            //                    d_p->print(",");
                            //                    std::cout << "_data:";
                            //                    for (uint64_t i = 0; i <
                            //                    d_p->_allocated_size - 1; ++i)
                            //                    {
                            //                        std::cout << d_p->_data[i]
                            //                        <<
                            //                        ',';
                            //                    }
                            //                    std::cout <<
                            //                    d_p->_data[d_p->_allocated_size
                            //                    - 1]
                            //                              << std::endl;
                            //                    std::cout << "_head-_tail
                            //                    delta:"
                            //                    << d_p->head_tail_delta()
                            //                              << std::endl;
                        } else {
                            throw ERROR;
                        }
                    } catch (char const* err) {
                        std::cout << err << std::endl;
                    } catch (...) {
                        std::cout << ERROR << std::endl;
                    }
                }
            }
        }
        std::getline(std::cin, cmdline);
    }
    if (is_running_flag) {
        delete d_p;
    }
    return 0;
}
