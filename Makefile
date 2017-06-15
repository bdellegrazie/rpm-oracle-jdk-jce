JDK_MAJOR:=8
ITERATION:=1
ARCH:=noarch
BUILD_DIR:=build

.PHONY: rpm rpm-clean build-clean dist-clean clean packages deps

all: packages

rpm-clean:
	rm -f *.rpm

build-clean:
	rm -rf $(BUILD_DIR)/*

clean: rpm-clean build-clean

dist-clean: clean
	rm -f *.zip

deps:
	curl --progress-bar -m 60 -L -o jce_policy-$(JDK_MAJOR).zip -C - --cookie 'oraclelicense=accept-securebackup-cookie' http://download.oracle.com/otn-pub/java/jce/$(JDK_MAJOR)/jce_policy-$(JDK_MAJOR).zip

rpm: clean
	mkdir -p $(BUILD_DIR)/BUILD
	mkdir -p $(BUILD_DIR)/BUILDROOT
	mkdir -p $(BUILD_DIR)/RPMS
	rpmbuild -bb -D'jdk_version_major $(JDK_MAJOR)'\
 -D'ITERATION $(ITERATION)'\
 -D'_builddir $(PWD)/$(BUILD_DIR)/BUILD'\
 -D'_rpmdir   $(PWD)/$(BUILD_DIR)/RPMS'\
 -D'_sourcedir $(PWD)'\
 -D'_buildrootdir $(PWD)/$(BUILD_DIR)/BUILDROOT'\
 jdk-jce.spec
	mv $(BUILD_DIR)/RPMS/noarch/*.rpm .

packages: rpm

