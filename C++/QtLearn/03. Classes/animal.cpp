#include "animal.h"

Animal::Animal(QObject *parent) : QObject(parent)
{
    qDebug() << this << " constructed\n";
}
