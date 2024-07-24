source env/bin/activate

export localhost_ip="$(hostname -I | awk '{print $1}')"

export environment="local"
echo "local-ip: [$localhost_ip] | environment: [$environment]"

export API_KEY="DA23ws213321232a2"
