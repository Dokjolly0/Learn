#ifndef ANIMAL_H
#define ANIMAL_H

#include "QObject"
#include "QtDebug"

class Animal : public QObject
{
    Q_OBJECT
public:
    explicit Animal(QObject *parent = nullptr);
signals:
};

#endif // ANIMAL_H
