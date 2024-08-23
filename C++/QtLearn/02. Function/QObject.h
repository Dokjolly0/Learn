#ifndef QOBJECT_H
#define QOBJECT_H

#include <QCoreApplication>

QObject &get_qt_obj(QString name){
    QObject obj;
    obj.setObjectName(name);
    return obj; //Sara eliminato //main.cpp:18:12: error: call to deleted constructor of 'QObject'
}

#endif // QOBJECT_H
