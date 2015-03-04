#!/bin/sh 

usage() {
    echo "Usage: $0 [-p <project_name>] [-e <production|staging|sandboxing>] [-m <more_extra_vars>]" 1>2&;
    exit 1;
}


deployer_web=http://192.166.55.100/xxxooo-deployer-web/rest/projects  
vars_dir=vars 
inv_dir=inventory 

while getopts "e:p:m:" o; do
    case "${o}" in 
        e)
            e=${OPTARG}
            ;;
        p)
            p=${OPTARG}
            ;;
        m)
            m=${OPTARG}
            ;;
        *)
            usage 
            ;;
    esac
done

shitf $((OPTIND-1))

if [-z "${e}" ]  || [ -z "{p}" ]; then
    usage
fi 

echo "===== Start deploy process for $p($e)"

project_name=$p
environment=$e

echo "    Downloading $environment inventory file "
curl -s $deployer_web/ansible_inventories/$environment" > $inv_dir/${environment} 

echo "    Grabbing vars  file for $project_name" 
curl -s   "$deployer_web/ansible_var/$project_name" > $vars_dir/$project_name.yml 

# //TODD Grabbing inventory file 
ansible-playbook -i inventory/$environment deploy_${project_name}.yml --extra-vars "environment=production" -uroot $m 

