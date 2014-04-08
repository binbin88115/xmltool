// THIS FILE IS GENERATED BY TOOL, PLEASE DON'T EDIT

#ifndef _XML_MANAGER_H_
#define _XML_MANAGER_H_

#include "XMLLoader.h"
#include "XMLData.h"

#define XML_VAR(TableName)			m_##TableName
#define XML_DECLARE_VAR(TableName)	XMLLoader<TableName##{3}> XML_VAR(TableName)
#define XML_DATASET(TableName)		XMLManager::sharedInstance().XML_VAR(TableName)
#define LOAD_XML_DATA()				XMLManager::sharedInstance().loadData()

class TiXmlDocument;
class XMLManager
{0}
protected:
	XMLManager();

public:
	~XMLManager();

	static XMLManager& sharedInstance();
	void loadData();

public:
{2}
protected:
	TiXmlDocument loadFromFile(const char* filename);

private:
	bool m_bInited;
{1};

#endif // _XML_MANAGER_H_
